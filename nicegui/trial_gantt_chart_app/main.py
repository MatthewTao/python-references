from datetime import datetime, timedelta

from nicegui import ui

import database
import gantt

database.init_db()

TABLE_COLUMNS = [
    {"name": "task_name",  "label": "Task",             "field": "task_name",  "align": "left", "sortable": True},
    {"name": "start_date", "label": "Start",            "field": "start_date", "sortable": True},
    {"name": "end_date",   "label": "End",              "field": "end_date",   "sortable": True},
    {"name": "duration",   "label": "Duration (days)",  "field": "duration",   "sortable": True},
    {"name": "depends_on", "label": "Depends On",       "field": "depends_on", "align": "left"},
    {"name": "actions",    "label": "",                 "field": "actions"},
]

# task_name -> end_date, kept in sync with DB on every refresh
task_end_dates: dict[str, str] = {t["task_name"]: t["end_date"] for t in database.get_all_tasks()}


def _to_display_rows(tasks: list[dict]) -> list[dict]:
    return [{**t, "depends_on": t["depends_on"] or ""} for t in tasks]


def handle_deps_change() -> None:
    selected: list[str] = depends_select.value or []
    if not selected:
        return
    latest = max(task_end_dates[n] for n in selected if n in task_end_dates)
    start_input.value = latest


def refresh() -> None:
    global task_end_dates
    tasks = database.get_all_tasks()
    task_end_dates = {t["task_name"]: t["end_date"] for t in tasks}

    chart.update_figure(gantt.build_gantt(tasks))

    table.rows[:] = _to_display_rows(tasks)
    table.update()

    depends_select.options = list(task_end_dates.keys())
    # Drop any selections that no longer exist
    depends_select.value = [v for v in (depends_select.value or []) if v in task_end_dates]
    depends_select.update()


def handle_add() -> None:
    name = name_input.value.strip()
    start = start_input.value
    selected_deps: list[str] = depends_select.value or []
    deps = ", ".join(selected_deps) if selected_deps else None

    if not name:
        ui.notify("Task name is required.", type="negative")
        return
    if not start:
        ui.notify("Start date is required.", type="negative")
        return
    try:
        duration = float(duration_input.value)
        if duration <= 0:
            raise ValueError
    except (TypeError, ValueError):
        ui.notify("Duration must be a positive number.", type="negative")
        return

    end = (datetime.strptime(start, "%Y-%m-%d") + timedelta(days=duration)).strftime("%Y-%m-%d")

    database.add_task(name, start, end, duration, deps)

    name_input.value = ""
    duration_input.value = None
    depends_select.value = []

    ui.notify(f"Task '{name}' added.", type="positive")
    refresh()


def handle_delete(task_id: int) -> None:
    database.delete_task(task_id)
    ui.notify("Task deleted.", type="warning")
    refresh()


# ── UI layout ─────────────────────────────────────────────────────────────────

with ui.column().classes("w-full max-w-7xl mx-auto p-4 gap-6"):

    ui.label("Gantt Chart App").classes("text-2xl font-bold")

    # Chart
    initial_tasks = database.get_all_tasks()
    chart = ui.plotly(gantt.build_gantt(initial_tasks)).classes("w-full").style("min-height: 300px")

    ui.separator()

    with ui.row().classes("w-full gap-6 items-start flex-wrap"):

        # ── Add task form ──────────────────────────────────────────────────
        with ui.card().classes("w-80"):
            ui.label("Add Task").classes("text-lg font-semibold mb-2")

            name_input = ui.input("Task Name").classes("w-full")

            with ui.input("Start Date (YYYY-MM-DD)") as start_input:
                start_input.classes("w-full")
                with ui.menu().props("no-parent-event") as start_menu:
                    with ui.date(mask="YYYY-MM-DD").bind_value(start_input):
                        with ui.row().classes("justify-end"):
                            ui.button("Close", on_click=start_menu.close).props("flat")
                with start_input.add_slot("append"):
                    ui.icon("edit_calendar").on("click", start_menu.open).classes("cursor-pointer")

            duration_input = ui.number("Duration (days)", min=1, precision=0).classes("w-full")

            depends_select = ui.select(
                options=list(task_end_dates.keys()),
                multiple=True,
                label="Depends On",
                on_change=handle_deps_change,
            ).classes("w-full").props("use-chips")

            ui.button("Add Task", on_click=handle_add).props("color=primary").classes("w-full mt-3")

        # ── Task table ─────────────────────────────────────────────────────
        with ui.card().classes("flex-1 min-w-0"):
            ui.label("Tasks").classes("text-lg font-semibold mb-2")

            table = ui.table(
                columns=TABLE_COLUMNS,
                rows=_to_display_rows(initial_tasks),
                row_key="id",
            ).classes("w-full")

            table.add_slot(
                "body-cell-actions",
                """
                <q-td :props="props">
                    <q-btn flat round color="negative" icon="delete" size="sm"
                           @click="$parent.$emit('delete-row', props.row)" />
                </q-td>
                """,
            )
            table.on("delete-row", lambda e: handle_delete(e.args["id"]))


if __name__ == "__main__":
    ui.run(title="Gantt Chart App", port=8080, reload=False, show=False)

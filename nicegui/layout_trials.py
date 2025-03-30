import datetime as dt
from nicegui import app, ui


def some_other_function():
    print(f"{dt.datetime.now().isoformat()} - function has run")


def read_from_storage():
    ui.notify(f'Note says: {app.storage.client["note"]}')


def shutdown():
    app.shutdown()
    ui.notify("Server has shutdown, you can close the window now")


@ui.page("/")
def index():
    with ui.row():
        with ui.card():
            ui.label("Card content")
            ui.button("Add label", on_click=lambda: ui.label("Click!"))
            ui.timer(5.0, some_other_function, once=False)

        with ui.card():
            ui.label("Another card")

    ui.textarea("This note is kept in temp storage").classes("w-full").bind_value(
        app.storage.client, "note"
    )
    ui.button("Reflect what's in the note above", on_click=read_from_storage)
    ui.separator()
    ui.button("End Server", on_click=shutdown)


if __name__ in {"__main__", "__mp_main__"}:
    ui.run(show=False, port=12345, dark=True)

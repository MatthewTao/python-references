# NiceGUI Gantt Chart App

A trial NiceGUI application that displays an interactive Plotly Gantt chart backed by a SQLite database.

## Purpose

Explore NiceGUI's capabilities by building a simple project task manager with:
- A Plotly Gantt chart that renders tasks from a SQLite database
- A form to add new tasks
- The ability to delete existing tasks

## Features

- **Interactive Gantt chart** — rendered with Plotly via NiceGUI's `ui.plotly` component
- **Today marker** — dashed red vertical line indicating the current date
- **Add tasks** — form inputs for task name, start date, duration, and dependencies
- **Derived end date** — end date is calculated automatically from start date + duration
- **Dependency selection** — multi-select dropdown listing existing tasks; selecting dependencies auto-sets the start date to the latest end date among them
- **Delete tasks** — remove tasks from the chart and database
- **Persistent storage** — all task data stored in a local SQLite file

## Task Fields

| Field | Type | Description |
|---|---|---|
| `task_name` | Text | Name of the task |
| `start_date` | Date | When the task begins (auto-set from dependencies if selected) |
| `end_date` | Date | Derived from start date + duration; stored in the database |
| `duration` | Number | Duration of the task in days (form input) |
| `depends_on` | Text | Comma-separated names of tasks this task depends on |

## Add Task Form

| Input | Type | Notes |
|---|---|---|
| Task Name | Text | Required |
| Start Date | Date picker | Auto-populated with latest dependency end date when dependencies are selected |
| Duration (days) | Number | Must be ≥ 1 |
| Depends On | Multi-select dropdown | Options are populated from existing tasks |

## Requirements

```
nicegui
plotly
pandas
```

Install dependencies:

```bash
pip install nicegui plotly pandas
```

## Running the App

```bash
python main.py
```

Then open your browser at `http://localhost:8080`.

## Project Structure

```
trial_gantt_chart_app/
├── main.py          # NiceGUI app entry point
├── database.py      # SQLite connection and CRUD operations
├── gantt.py         # Plotly Gantt chart builder
├── tasks.db         # SQLite database file (auto-created)
└── README.md
```

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "tasks.db"


def init_db() -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                task_name   TEXT    NOT NULL,
                start_date  TEXT    NOT NULL,
                end_date    TEXT    NOT NULL,
                duration    REAL    NOT NULL,
                depends_on  TEXT
            )
        """)


def get_all_tasks() -> list[dict]:
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute(
            "SELECT id, task_name, start_date, end_date, duration, depends_on "
            "FROM tasks ORDER BY start_date, task_name"
        )
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]


def add_task(task_name: str, start_date: str, end_date: str,
             duration: float, depends_on: str | None) -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO tasks (task_name, start_date, end_date, duration, depends_on) "
            "VALUES (?, ?, ?, ?, ?)",
            (task_name, start_date, end_date, duration, depends_on),
        )


def delete_task(task_id: int) -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

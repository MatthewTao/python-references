import sqlite3
from flask import current_app, g


def init_app(app):
    app.teardown_appcontext(close_db)
    with app.app_context():
        init_db_command()


def init_db_command():
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf-8"))


def get_db():
    if "db" not in g:
        # Connect to the db if a connection doesn't already exist
        g.db = sqlite3.connect(
            current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES,
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

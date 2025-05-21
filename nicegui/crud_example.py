from nicegui import ui
import sqlite3


conn = sqlite3.connect("example_db.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS "users" (
	"id"	INTEGER,
	"name"	TEXT,
	"age"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
"""
)

name = ui.input(label="name").classes("w-full")
age = ui.input(label="age").classes("w-full")
get_id = ui.label()


def clear_fields():
    name.value = ""
    age.value = ""
    get_id.text = ""


def save_and_edit_row(row):
    try:
        query = """UPDATE users SET name=?, age=? WHERE id=?"""
        cursor.execute(query, (edit_name.value, edit_age.value, get_id.text))
        conn.commit()
        ui.notify("Updated row")

        edit_dialog.close()
        all_data.clear()
        clear_fields()
        get_all_data()
    except Exception as e:
        print(repr(e))
    ui.update(all_data)


with ui.dialog() as edit_dialog:
    with ui.card():
        ui.label("Edit Row").classes("font-xl font-weight")

        edit_name = ui.input().bind_value_from(name, "value")
        edit_age = ui.input().bind_value_from(age, "value")

        with ui.row().classes("justify-between"):
            ui.button("Save", on_click=lambda e: save_and_edit_row(e))
            ui.button("Close", on_click=edit_dialog.close()).classes("bg-red")


def edit_row(row):
    get_id.text = row.default_slot.children[0].text
    name.value = row.default_slot.children[1].text
    age.value = row.default_slot.children[2].text

    edit_dialog.open()
    ui.update()


def delete_row(row):
    cursor.execute(
        """DELETE FROM users WHERE id=?""", (row.default_slot.children[0].text,)
    )
    conn.commit()
    all_data.clear()
    clear_fields()
    get_all_data()
    ui.notify("Deleted row")


def get_all_data():
    cursor.execute("""SELECT * FROM users""")
    result = cursor.fetchall()

    all_data_list = []
    # Convert result into list of dict
    for row in result:
        data = {}
        for i, col in enumerate(cursor.description):
            data[col[0]] = row[i]
        all_data_list.append(data)
    print(all_data_list)
    for x in all_data_list:
        with all_data:
            with ui.card():
                with ui.row().classes("justify-between w-full") as card_data:
                    ui.label(x["id"])
                    ui.label(x["name"])
                    ui.label(x["age"])

                with ui.row():
                    # I don't really understand what's going on in these lines yet
                    ui.button("edit").on(
                        "click", lambda e, card_data=card_data: edit_row(card_data)
                    ).classes("bg-blue")
                    ui.button("delete").on(
                        "click", lambda e, card_data=card_data: delete_row(card_data)
                    ).classes("bg-red")


def add_new_row():
    try:
        cursor.execute(
            """INSERT INTO users (name, age) VALUES (?, ?)""", (name.value, age.value)
        )
        conn.commit()
        ui.notify("Added row", color="green")

        clear_fields()

        all_data.clear()
        get_all_data()
    except Exception as e:
        print(repr(e))


ui.button("New Row", on_click=add_new_row)
all_data = ui.column()

all_data.clear()
get_all_data()
ui.run(show=False)

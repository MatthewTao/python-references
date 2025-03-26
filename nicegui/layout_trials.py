from nicegui import ui


def some_other_function():
    print("something")


with ui.row():
    with ui.card():
        ui.label("Card content")
        ui.button("Add label", on_click=lambda: ui.label("Click!"))
        ui.timer(15.0, some_other_function, once=False)

    with ui.card():
        ui.label("Another card")


if __name__ in {"__main__", "__mp_main__"}:
    ui.run(show=False)

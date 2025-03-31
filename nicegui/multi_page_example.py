from nicegui import ui

@ui.page('/', dark=True)
def home():
    ui.label('Welcome to the home page')
    ui.link('Visit dark page', new_entry)


@ui.page('/new_entry', dark=True)
def new_entry():
    ui.label('Welcome to the new entry page')
    ui.button("Go to home", on_click=lambda: ui.notify("saved data or something"))


ui.run(show=False, native=True)

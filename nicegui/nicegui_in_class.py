from nicegui import app, ui


class GUI:
    def __init__(self):
        # ui logic can go here
        ui.label("GUI defined in a class")
        ui.button("Click me", on_click=lambda: self.clicker())
        ui.button("Shutdown Server", on_click=self.shutdown)

    @staticmethod
    def clicker():
        ui.notify("Clicked")

    @staticmethod
    def shutdown():
        app.shutdown()


@ui.page("/")
def main():
    gui = GUI()


ui.run(port=28842, reload=False)

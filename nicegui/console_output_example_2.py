import logging
from datetime import datetime
from nicegui import app, ui

logger = logging.getLogger()


class LogElementHandler(logging.Handler):
    """A logging handler that emits messages to a log element."""

    def __init__(self, element: ui.log, level: int = logging.NOTSET) -> None:
        self.element = element
        super().__init__(level)

    def emit(self, record: logging.LogRecord) -> None:
        try:
            msg = self.format(record)
            self.element.push(msg)
        except Exception:
            self.handleError(record)


@ui.page("/page")
def page():
    log = ui.log(max_lines=1000).classes("w-full")
    page_log_handler = LogElementHandler(log)
    logger.addHandler(page_log_handler)
    ui.context.client.on_disconnect(lambda: logger.removeHandler(page_log_handler))
    ui.button(
        "Log time",
        on_click=lambda: logger.warning(datetime.now().strftime("%X.%f")[:-5]),
    )


if __name__ == "__main__":
    main_log = ui.log(max_lines=1000).classes("w-full")
    nicegui_log_handler = LogElementHandler(main_log)
    logger.addHandler(nicegui_log_handler)
    ui.button(
        "Log time", on_click=lambda: logger.warning(datetime.now().isoformat()[:-5])
    )

    def handle_shutdown():
        logger.removeHandler(nicegui_log_handler)

    app.on_shutdown(handle_shutdown)
    ui.run(reload=False, dark=True, show=False)

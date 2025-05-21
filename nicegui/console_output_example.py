from nicegui import ui, app
import time
import asyncio
import sys
from io import StringIO

from logging import getLogger, StreamHandler

logger = getLogger(__name__)
logger.setLevel("DEBUG")


# Backend
def long_sync_func():
    """A synchronous function with a lot of printing or logging."""
    for _ in range(3):
        time.sleep(5)
        print("Hi there from a print.")
        logger.info("Hi from a logger.")
    raise Exception("Uh oh this is an exception.")


# Frontend
async def button_callback():
    """Called after button click"""
    await asyncio.to_thread(long_sync_func)


async def start_stream():
    """Start a 'stream' of console outputs."""
    # Create buffer
    string_io = StringIO()

    # Standard output like a print
    # sys.stdout = string_io  # Not sure why the stdout adds like an additional indent for like each line
    # I guess the ideal for this case would probably be to use logging to control what gets pushed.

    # Errors/Exceptions
    sys.stderr = string_io

    # Log Messages
    stream_handler = StreamHandler(string_io)
    stream_handler.setLevel("DEBUG")
    logger.addHandler(stream_handler)
    while 1:
        await asyncio.sleep(1)  # need to update ui
        # Push the log component and reset the buffer
        log.push(string_io.getvalue())
        string_io.truncate(0)


if __name__ == "__main__":
    button = ui.button("Callback", on_click=button_callback)
    log = ui.log(100).classes("w-full").style("height: 500px")
    app.on_startup(start_stream)
    ui.run(reload=False, dark=True, show=False)

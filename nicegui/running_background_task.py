import asyncio
from nicegui import ui, background_tasks


async def long_running_task(log_callback):
    for i in range(10):
        await asyncio.sleep(1)
        log_callback(f"Log line {i+1}")
        log_callback("Task completed!")


async def auto_start_background_task():
    print("Starting background task...")
    while True:
        await asyncio.sleep(5)
        print("Background task is running...")


@ui.page("/", dark=True)
def index():
    background_tasks.create(auto_start_background_task())
    log_area = ui.log().props("readonly").style("width: 100%; height: 300px;")

    def append_log(message):
        log_area.push(message)

    async def start_task():
        background_tasks.create(long_running_task(append_log))

    ui.button("Start Background Task", on_click=start_task)


if __name__ == "__main__":
    ui.run(reload=False, show=False)

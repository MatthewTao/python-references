import pyautogui as pg
from nicegui import ui


def press_up():
    pg.press("up")


ui.button("Press up", on_click=press_up)


ui.run(show=False, host="0.0.0.0", dark=True, title="Key Presser")

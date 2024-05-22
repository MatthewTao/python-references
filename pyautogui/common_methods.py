from pyscreeze import ImageNotFoundException

import pyautogui
import time


def find_button(path_to_image, confidence=0.9, delay=0.5, attempts=5):
    buttonx = None
    buttony = None
    tries = 0
    while buttonx is None:
        try:
            location = pyautogui.locateOnScreen(path_to_image, confidence=confidence)
            buttonx, buttony = pyautogui.center(location)
        except ImageNotFoundException:
            # If button can't be found, wait a bit
            time.sleep(delay)
            tries += 1
            if tries > attempts:
                break
        else:
            # Button is found, break and return
            break

    if buttonx is None:
        raise Exception("Button not found")
    return buttonx, buttony


def click_button(path_to_image):
    x, y = find_button(path_to_image)
    pyautogui.click(x, y)

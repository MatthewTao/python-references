from pyautogui import alert


def alert_box(text="", title="", button="OK"):
    alert(text=text, title=title, button=button)


if __name__ == "__main__":
    alert_box(title="Notification test", text="Testing Notifications")

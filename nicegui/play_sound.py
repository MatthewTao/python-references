from nicegui import ui

notification_sound = ui.audio("./notification.mp3", controls=False)


def play_sound():
    notification_sound.play()


ui.button("Play sound", on_click=play_sound)


if __name__ == "__main__":
    ui.run(show=False, reload=False, port=9823)

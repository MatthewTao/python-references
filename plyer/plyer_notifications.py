from plyer import notification


notification.notify(
    title='Here is the title within the notification',
    message='Here is the message',
    app_icon=None,  # e.g. 'C:\\icon_32x32.ico'
    app_name='plyer test --> This seems to have no effect in win10',
    ticker='plyer test This seems to have no effect in win10',
    timeout=10,  # seconds
)

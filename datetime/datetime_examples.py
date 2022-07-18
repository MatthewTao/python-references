from datetime import datetime


def get_datetime_iso_str():
    """
    Returns the current datetime as a ISO formated datetime string
    %y-%m-%dT%H:%M.%f
    """
    now = datetime.now()
    str_fmt = now.isoformat()
    return str_fmt


if __name__ == '__main__':
    print(get_datetime_iso_str())

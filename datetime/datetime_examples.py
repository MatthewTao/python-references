from datetime import datetime


def get_datetime_iso_str():
    """
    Returns the current datetime as a ISO formated datetime string
    %y-%m-%dT%H:%M.%f
    """
    now = datetime.now()
    str_fmt = now.isoformat()
    return str_fmt


def get_datetime_as_string(fmt="%Y-%m-%dT%H:%M:%S.%f"):
    now = datetime.now()
    str_fmt = now.strftime(fmt)
    return str_fmt

def convert_seconds_left_to_str(seconds_left):
    """
    Returns the number of minutes and seconds left when given a second countdown
    """
    minutes_left = int(seconds_left // 60)
    seconds_left = int(seconds_left - minutes_left * 60)
    return f'{minutes_left} mins {seconds_left} secs'


def convert_datetime_to_epoch(datetime_str, datetime_format='%d/%m/%Y'):
    datetime_obj = datetime.strptime(datetime_str, datetime_format)
    timestamp = int(datetime.timestamp(datetime_obj))
    return timestamp


if __name__ == '__main__':
    print(get_datetime_iso_str())
    print(get_datetime_as_string())

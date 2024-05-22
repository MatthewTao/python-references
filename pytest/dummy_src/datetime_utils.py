from datetime import datetime, timezone


def datetime_to_string(string: str, timezone: timezone = None):
    """
    Use strftime to put datetime into a string
    :param string: normally it is a s3 object prefix, should look like 'xxx/%Y-%m-%d'
    :param timezone: a timezone object in python datetime
    :return: str
    """
    now = datetime.now(tz=timezone)
    return now.strftime(string)


def combine_date_and_time(
    str_date: str, date_format: str, str_time: str, time_format: str
) -> tuple:
    """
    combines a date and time field into a datetime

    :param str str_date: date as a string
    :param str date_format: format of date
    :param str str_time: time as a string
    :param str time_format: format of time
    :return: a combined datetime string of format '{date_format}T{time_format}'
    """
    combined_datetime = "T".join([str_date, str_time])
    combined_datetime_format = "T".join([date_format, time_format])

    return combined_datetime, combined_datetime_format


def string_datetime_to_epoch(str_datetime: str, str_format: str = None) -> int:
    """
    Given a string datetime and it's format, epoch will be returned
    :param str_datetime: datetime in str representation
    :param str_format: format of datetime
    :return: epoch in seconds
    """
    if isinstance(str_datetime, str):
        if not str_format:
            str_format = "%Y-%m-%d T%H:%M:%S.%f"
        datetime_object = datetime.strptime(str_datetime, str_format)
        epoch_time = int((datetime_object - datetime(1970, 1, 1)).total_seconds())
        return epoch_time
    else:
        # Method only works with strings
        raise TypeError(
            f"string_datetime_to_epoch only works with strings, "
            f"received {str_datetime}, {type(str_datetime)}"
        )


def epoch_to_str(epoch: int, str_format: str) -> str:
    """
    Given an epoch in seconds, a datetime as a string will be returned
    """
    str_datetime = datetime.utcfromtimestamp(epoch).strftime(str_format)
    return str_datetime

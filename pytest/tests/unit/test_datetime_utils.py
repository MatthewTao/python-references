import pytest

from dummy_src.datetime_utils import (combine_date_and_time, epoch_to_str, string_datetime_to_epoch)

unify_date_time_formats_test_data = [
    ('2019/06/23 23:45:38', '%Y/%m/%d %H:%M:%S', '%Y%m%d%H', '2019062323'),
    ('2014-07-04 11:51:54', '%Y-%m-%d %H:%M:%S', '%Y%m%d%H', '2014070411')
]


# @pytest.mark.parametrize(
#     'datetime, datetime_format, output_format, expected', unify_date_time_formats_test_data
# )
# def test_change_date_time_formats(datetime, datetime_format, output_format, expected):
#     """
#     | Given a datetime as a string in a known format
#     | When a desired format is provided,
#     | Then the datetime can be reformatted
#     """

#     changed_time = change_datetime_format(**{'str_datetime': datetime,
#                                              'datetime_format': datetime_format,
#                                              'output_format': output_format})

#     assert changed_time == expected


combine_date_and_time_test_data = [
    ('2019/06/23', '%Y/%m/%d', '23:45:38', '%H:%M:%S', '2019/06/23T23:45:38'),
    ('2014-07-04', '%Y-%m-%d', '11:51:54', '%H:%M:%S', '2014-07-04T11:51:54')
]


@pytest.mark.parametrize(
    'date, date_format, time, time_format, expected', combine_date_and_time_test_data
)
def test_combine_date_and_time(date, date_format, time, time_format, expected):
    """
    | Given a date string and a time string, with known formats,
    | When a desired datetime string format is provided,
    | Then the date and time can be combined into a datetime string
    """
    combined_datetime, combined_datetime_format = combine_date_and_time(date, date_format, time, time_format)

    assert combined_datetime == expected


# @pytest.mark.parametrize(
#     'date_time_format, expected', [
#         ('YYYY-MM-DD', '%Y-%m-%d'),
#         ('YYYY/MM/DDTHH:mm:ss', '%Y/%m/%dT%H:%M:%S'),
#         ('hh:mm:ssAM/PM', '%I:%M:%S%p')
#     ]
# )
# def test_reformat_date_time_format(date_time_format, expected):
#     """
#     | Given a human readable date time format e.g. 'YYYY-MM-DD'
#     | Then a datetime datetime format will be returned
#     """
#     formatted_date_time_format = reformat_date_time_format(date_time_format)

#     assert formatted_date_time_format == expected


@pytest.mark.parametrize(
    'epoch, str_format, expected_datetime', [
        (1546383684, '%Y-%m-%d T%H:%M:%S', '2019-01-01 T23:01:24'),
        (1546300800, '%Y-%m-%d T%H:%M:%S', '2019-01-01 T00:00:00'),
        (1546383684, '%Y-%m-%d T%H:%M:%S.%f', '2019-01-01 T23:01:24.000000'),
        (1546300800, '%Y-%m-%d T%H:%M:%S.%f', '2019-01-01 T00:00:00.000000')
    ]
)
def test_epoch_conversions(epoch, str_format, expected_datetime):
    """
    Test will convert epoch to datetime string,
    then from datetime string back to epoch.
    assert that the starting epoch is equal to the final epoch
    """
    str_datetime = epoch_to_str(epoch, str_format=str_format)
    assert str_datetime == expected_datetime
    print(str_datetime)

    resulting_epoch = string_datetime_to_epoch(str_datetime, str_format=str_format)
    assert epoch == resulting_epoch

from typing import Union
import numpy as np


def count_days_in_period(start_period: Union[str, np.datetime64], end_period: str) -> np.timedelta64:
    """
    Calculate days between start to end.
    :param start_period: Start period.
    :param end_period: End period.
    :return: How many days there are between start period to end period.
    """
    return np.datetime64(end_period) - np.datetime64(start_period)


def count_special_days_for_me() -> None:
    """
    its note connect to the exercise, but I wanted to see some
    things in np.date.
    np.datetime64('today') will give you the date of today.
    Also there is some different between np.datetime64 and np.timedelta64.
    https://www.geeksforgeeks.org/get-the-dates-of-yesterday-today-and-tomorrow-using-numpy/
    """
    print("Number of days, to end of semester: ")
    print(np.datetime64('today'))
    print(count_days_in_period(np.datetime64('today'), '2022-06-17'))
    print("Number of days, to end of exams period: ")
    print(count_days_in_period(np.datetime64('today'), '2022-07-14'))
    print("Number of days, to end of all my studies: ")
    print(count_days_in_period(np.datetime64('today'), '2022-09-01'))


def main() -> None:
    """
    Count days between two dates.
    """
    print(count_days_in_period('2016-02-01', '2016-03-01'))
    count_special_days_for_me()


if __name__ == '__main__':
    main()

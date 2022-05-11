import numpy as np


def change_sign_in_range(arr: np.array, start_range: int, end_range: int) -> None:
    """
    Change the sign of the numbers in the range from min_range to max_range.
    :param arr: Arr to be changed.
    :param start_range: Start range.
    :param end_range: End range.
    """
    arr[start_range:end_range] *= -1


def main() -> None:
    """
    Create a vector with values from 0 to 20
    and change the sign of the numbers in the range from 9 to 15.
    """
    arr = np.arange(20)
    change_sign_in_range(arr, 9, 15)
    print(arr)


if __name__ == '__main__':
    main()

import numpy as np
import nptyping


def create_combination(one_d_array: nptyping.ndarray, two_d_array: nptyping.ndarray) -> list:
    """
    Combine one_d_array and two_d_array by indexes.
    For example:
    [1, 2, 3]
    [[10,  20,   30]
     [100, 200, 300]]
    The result will be:
    1:10 2:20 3:30 1:100 2:200 3:300.

    Go over all values using iterator.
    The iterator goes over line after line and stop when
    the bigger array finish.
    Each iteration in the loop we get the same index in the line (1:1, 2:2, 3:3 and so on).
    The loop will finish when the iterator arrive to last row in the biggest array.
    (in our example - 2).
    :param one_d_array: To combine.
    :param two_d_array: To combine.
    :return: New list with all values as a string.
    """
    return [(str(a) + ":" + str(b)) for a, b in np.nditer([one_d_array, two_d_array])]


def main() -> None:
    """
    Create 1-D and 2-D array, combine them by indexes,
    and show the combination.

    """
    one_d_array = np.arange(4)
    two_d_array = np.arange(8).reshape(2, 4)
    print(create_combination(one_d_array, two_d_array))


if __name__ == '__main__':
    main()

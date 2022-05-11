import numpy as np


def replace_all_values_are_equal(matrix, old_val, new_val):
    """
    Replace all values are equal to old_val with new_val.
    :param matrix: Matrix to work with.
    :param old_val: Value to replace.
    :param new_val: New value to swap with old val.
    :return: New matrix with all values are equal to old_val with new_val.
    """
    return np.where(matrix == old_val, new_val, matrix)


def replace_all_values_are_less(matrix, old_val, new_val):
    """
    Replace all values are less than old_val with new_val.
    :param matrix: Matrix to work with.
    :param old_val: Value to replace.
    :param new_val: New value to swap with old val.
    :return: New matrix with all values are less than old_val with new_val.
    """
    return np.where(matrix < old_val, new_val, matrix)


def replace_all_values_are_greater(matrix, old_val, new_val):
    """
    Replace all values are greater than old_val with new_val.
    :param matrix: Matrix to work with.
    :param old_val: Value to replace.
    :param new_val: New value to swap with old val.
    :return: New matrix with all values are greater than old_val with new_val.
    """
    return np.where(matrix > old_val, new_val, matrix)


def main() -> None:
    """
    https://www.w3resource.com/python-exercises/numpy/basic/numpy-basic-exercise-54.php
    Create matrix and Replace all numbers in a given matrix
    which is equal, less and greater to a given number.
    """
    matrix = np.arange(1, 10).reshape(3, 3)
    old_val = 5
    new_val = -5
    print(replace_all_values_are_equal(matrix, old_val, new_val))
    print(replace_all_values_are_less(matrix, old_val, new_val))
    print(replace_all_values_are_greater(matrix, old_val, new_val))


if __name__ == '__main__':
    main()

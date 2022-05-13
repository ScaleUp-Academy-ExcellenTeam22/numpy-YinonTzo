import numpy as np
import nptyping


def convert_one_dimension_to_one(one_dimension_array_a: nptyping.ndarray,
                                 one_dimension_array_b: nptyping.ndarray) -> nptyping.ndarray:
    """
    https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-60.php
    :param one_dimension_array_a: First array to convert.
    :param one_dimension_array_b: second array to convert.
    :return: New 2-D array with array1 in row 0 and array b in row 1.
    """
    return np.dstack((one_dimension_array_a, one_dimension_array_b))


def main() -> None:
    """
    Create two 1-D array and convert them to 2-D array.
    """
    one_dimension_array_a = np.array([[10], [20], [30]])
    one_dimension_array_b = np.array([[40], [50], [60]])
    print(convert_one_dimension_to_one(one_dimension_array_a, one_dimension_array_b))


if __name__ == '__main__':
    main()

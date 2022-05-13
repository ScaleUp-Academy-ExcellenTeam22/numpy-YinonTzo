import numpy as np
import nptyping


def sort_along_axis(matrix: nptyping.ndarray, axis: int = 0) -> nptyping.ndarray:
    """
    Sort matrix along axis.
    :param matrix: To sort.
    :param axis: To sort along. If not given, it would sort by axis = 0
    :return: Sorted metrix.
    """
    return np.sort(matrix, axis=axis)


def main() -> None:
    """
    I learned about numpy axis from here.
    https://www.sharpsightlabs.com/blog/numpy-axes-explained/
    Create a matrix and sort it once by first axis and once by last axis.
    """
    matrix = np.array([[200, 5], [40, 6]])
    print(sort_along_axis(matrix, 0))
    print(sort_along_axis(matrix, 1))


if __name__ == '__main__':
    main()

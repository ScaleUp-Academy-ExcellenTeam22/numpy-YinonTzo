import numpy as np
import nptyping


def find_row_col(matrix: nptyping.ndarray) -> tuple[int, int]:
    """
    Find the number of rows and columns of a given matrix.
    :param matrix: Matrix to find her shapes.
    :return: tuple of row and col
    """
    return matrix.shape


def main() -> None:
    """
    Find the number of rows and columns of a given matrix.
    """
    matrix = np.arange(1, 10).reshape((3, 3))

    row, col = find_row_col(matrix)
    print(row, col)


if __name__ == '__main__':
    main()

import numpy as np
import nptyping


def main() -> None:
    """
    Create 2 matrix and multiply them element by element
    """
    matrix1 = np.arange(16).reshape(4, 4)
    matrix2 = np.arange(16, 32).reshape(4, 4)
    print(multiply_matrix_element_by_element(matrix1, matrix2))


def multiply_matrix_element_by_element(matrix1: nptyping.ndarray,
                                       matrix2: nptyping.ndarray) -> nptyping.ndarray:
    """
    https://numpy.org/doc/stable/reference/generated/numpy.multiply.html
    :param matrix1: First matrix to be multiplied.
    :param matrix2: second matrix to be multiplied.
    :return: New matrix with all element from matrix1 and matrix2 multiplied.
    """
    return np.multiply(matrix1, matrix2)


if __name__ == '__main__':
    main()


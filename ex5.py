import numpy as np
import nptyping


def main() -> None:
    """
    Add a vector to each row of a given matrix.
    """
    matrix = np.eye(6)
    vector = np.ones(6)
    print(add_vector_to_matrix(matrix, vector))


def add_vector_to_matrix(matrix: nptyping.ndarray, vector: nptyping.ndarray) -> nptyping.ndarray:
    """
    Add a vector to each row of a given matrix.
    :param matrix: Matrix for adding a vector.
    :param vector: Vector to add.
    :return: matrix + vector
    """
    return matrix + vector


if __name__ == '__main__':
    main()


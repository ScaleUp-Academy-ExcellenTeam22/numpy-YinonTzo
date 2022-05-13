import numpy as np
import nptyping


def main() -> None:
    """
    Create a 4x4 array with random values,
    now create a new array from the said array swapping first and last rows.
    """
    matrix = np.random.rand(4, 4)
    print(swap_matrix(matrix))


def swap_matrix(matrix: nptyping.ndarray) -> nptyping.ndarray:
    """
    Swap matrix.
    :param matrix: Matrix to swap.
    :return: Swapped matrix.
    """
    return matrix[::-1]


if __name__ == '__main__':
    main()

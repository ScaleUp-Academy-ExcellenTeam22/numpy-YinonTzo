import numpy as np
import nptyping


def delete_single_dimensional(matrix: nptyping.ndarray) -> nptyping.ndarray:
    """
    Remove single-dimensional entries from a specified shape.
    Return copy of matrix to avoid from side effect -
    the matrix before np.squeeze() and the matrix after np.squeeze()
    shared their memory.
    :param matrix: To delete single-dimensional.
    :return: Copy of matrix but without any single-dimensional.
    """
    return np.squeeze(matrix).copy()


def main() -> None:
    """
    Remove single-dimensional entries from a specified shape.
    Specified shape: (3, 1, 4)
    Expected Output: (3, 4)

    I read what it means to delete dimensional from here:
    https://note.nkmk.me/en/python-numpy-squeeze/
    """
    matrix = np.zeros((2, 1, 3))
    print("Before:\n", matrix)
    print("After:\n", delete_single_dimensional(matrix))


if __name__ == '__main__':
    main()

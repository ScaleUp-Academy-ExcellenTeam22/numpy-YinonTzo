import numpy as np
import nptyping


def create_eye_matrix(n: int) -> nptyping.ndarray:
    """
    Create identity matrix.
    :param n: nXn matrix.
    :return: identity matrix with size n.
    """
    return np.eye(n)


def main() -> None:
    """
    Create a 3-D array with ones on a diagonal and zeros elsewhere.
    """
    print(create_eye_matrix(3))


if __name__ == '__main__':
    main()

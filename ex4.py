import numpy as np


def main() -> None:
    """
    create a 10x10 matrix,
    in which the elements on the borders will be equal to 1, and inside 0
    """
    x = np.ones((10, 10))
    x[1:-1, 1:-1] = 0
    print(x)


if __name__ == '__main__':
    main()

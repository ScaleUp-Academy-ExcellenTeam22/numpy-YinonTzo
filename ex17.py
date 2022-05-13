import numpy as np


def main() -> None:
    """
    Create an array and compute the median.
    """
    array = np.arange(12)
    median = np.median(array)
    print(median)


if __name__ == '__main__':
    main()


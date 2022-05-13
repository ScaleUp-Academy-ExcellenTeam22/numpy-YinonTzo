import numpy as np
import nptyping


def create_evently_distributed_vector(length: int, min_value: int, max_value: int) -> nptyping.ndarray:
    """
    Create a vector of length 'length' with values evenly distributed
    between min_value and max_value.
    :param length: Vector length.
    :param min_value: Min value.
    :param max_value: Max value.
    :return: Num py array in length between min_value to max_value.
    """
    return np.linspace(min_value, max_value, length)


def main():
    """
    Create a vector of length 10 with values evenly distributed
    between 5 and 50.
    """
    print(create_evently_distributed_vector(10, 5, 50))


if __name__ == '__main__':
    main()

import numpy as np


def main() -> None:
    """
    create a three-dimension array with shape (300,400,5) and set to a variable.
    Fill the array elements with values using unsigned integer (0 to 255).
    https://www.w3resource.com/python-exercises/numpy/python-numpy-random-exercise-17.php
    """
    np.random.seed(32)
    nums = np.random.randint(low=0, high=256, size=(300, 400, 5), dtype=np.uint8)
    print(nums)


if __name__ == '__main__':
    main()

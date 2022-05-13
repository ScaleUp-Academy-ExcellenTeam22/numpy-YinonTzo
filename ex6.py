import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    """
    https://www.w3resource.com/python-exercises/numpy/basic/numpy-basic-exercise-40.php
    Write a NumPy program to compute the x and y coordinates for points on a sine curve
    and plot the points using matplotlib.
    """
    # Compute the x and y coordinates for points on a sine curve
    x = np.arange(0, 3 * np.pi, 0.2)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    main()

import numpy as np
from load_image import ft_load
from matplotlib import pyplot as plt


def ft_invert(array) -> np.array:
    """ Inverts the color of the image received."""
    old_array = np.array(array)
    new_arr = 255 - old_array
    plt.imshow(new_arr)
    plt.show()


def ft_red(array) -> np.array:
    """Keeps only the red channel of the image."""
    old_array = np.array(array)
    old_array[:, :, 1] = 0
    old_array[:, :, 2] = 0
    plt.imshow(old_array)
    plt.show()


def ft_green(array) -> np.array:
    """Keeps only the green channel of the image."""
    old_array = np.array(array)
    old_array[:, :, 0] = 0
    old_array[:, :, 2] = 0
    plt.imshow(old_array)
    plt.show()


def ft_blue(array) -> np.array:
    """Keeps only the blue channel of the image."""
    old_array = np.array(array)
    old_array[:, :, 0] = 0
    old_array[:, :, 1] = 0
    plt.imshow(old_array)
    plt.show()


def ft_grey(array) -> np.array:
    """Converts the image to grayscale."""
    zoomed = array[:, :, 1]

    plt.imshow(zoomed, cmap="gray")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


def main():
    """Loads the image and applies a filter."""
    array = ft_load("landscape.jpg")
    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)

    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()

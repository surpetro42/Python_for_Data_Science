import numpy as np
from matplotlib import pyplot as plt
from load_image import ft_load


def zoom(load: np.array, size: int, channel: int):
    """Zooms in on the selected part of the image."""
    h, w, _ = load.shape
    center_y = h // 2
    center_x = w // 2

    start_y = center_y - size // 2
    end_y = center_y + size // 2
    start_x = center_x - size // 2
    end_x = center_x + size // 2

    zoomed = load[start_y:end_y, start_x:end_x]
    zoomed = zoomed[:, :, channel]
    print("New shape after slicing:", zoomed.shape)
    print(zoomed)

    plt.imshow(zoomed, cmap="gray")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


def main():
    """Loads the image and displays the zoomed part."""
    load = ft_load("animal.jpeg")
    zoom(load, size=400, channel=1)


if __name__ == "__main__":
    main()

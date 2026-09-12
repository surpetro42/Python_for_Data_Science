import numpy as np
from matplotlib import pyplot as plt
from load_image import ft_load


def rotate(load: np.array, size: int, channel: int):
    h, w, _ = load.shape
    center_y = h // 2
    center_x = w // 2

    start_y = center_y - size // 2
    end_y = center_y + size // 2
    start_x = center_x - size // 2
    end_x = center_x + size // 2

    rotated = load[start_y:end_y, start_x:end_x]
    rotated = rotated[:, :, channel]
    print("New shape after slicing:", rotated.shape)
    new_rotated_transpose = np.zeros(rotated.shape)

    for i in range(len(rotated)):
        for j in range(len(rotated[i])):
            new_rotated_transpose[j][i] = rotated[i][j]
    # rotated = np.transpose(rotated)
    print(new_rotated_transpose)

    plt.imshow(new_rotated_transpose, cmap="gray")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


def main():
    load = ft_load("animal.jpeg")
    rotate(load, size=400, channel=1)


if __name__ == "__main__":
    main()

import numpy as np
from load_image import ft_load
from matplotlib import pyplot as plt

# invert: =, +, -, *
# red: =, *
# green: =, -
# blue: =
# grey: =, /


def ft_invert(array) -> np.array:
    """ Inverts the color of the image received."""
    old_array = np.array(array)
    new_arr = 255 - old_array 
    plt.imshow(new_arr)
    plt.show()

def ft_red(array) -> np.array:
    old_array = np.array(array)
    old_array[ :, :, 1] = 0
    old_array[ :, :, 2] = 0
    plt.imshow(old_array)
    plt.show()
    

def ft_green(array) -> np.array:
    old_array = np.array(array)
    old_array[ :, :, 0] = 0
    old_array[ :, :, 2] = 0
    plt.imshow(old_array)
    plt.show()

def ft_blue(array) -> np.array:
    old_array = np.array(array)
    old_array[ :, :, 0] = 0
    old_array[ :, :, 1] = 0
    plt.imshow(old_array)
    plt.show()


def ft_grey(array) -> np.array:
    # for i in array:
    #     for j in array[i]:
    #         count += array[i][j]
            

    grey = int((array[:, :, 0] + array[:, :, 1] + array[:, :, 2]) / 3)
    
    print(grey)
    plt.imshow(grey)
    plt.show()
    


def main():
    array = ft_load("landscape.jpg")
    array.shape
    print(array)
    # ft_invert(array)
    # ft_red(array)
    # ft_green(array)
    # ft_blue(array)
    ft_grey(array)

    # print(ft_invert.__doc__)
    # pass

if __name__ == "__main__":
    main()
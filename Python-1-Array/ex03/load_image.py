import numpy as np
from PIL import Image


def valid_format(path: str) -> bool:
    """Check that the path has a jpg or jpeg extension."""
    if not isinstance(path, str):
        print(type(path))
        raise ValueError("The path type is incorrect.")
    if path is None or path == "":
        raise ValueError("The path must not be empty.")

    spl_path = path.split(".")

    if len(spl_path) < 2 or spl_path[-1] == "":
        raise ValueError("The path must have an extension.")

    if spl_path[-1].lower() not in ("jpg", "jpeg"):
        raise ValueError("This path is wrong.")
    return True


def ft_load(path: str) -> np.array:
    """Load a JPG or JPEG image and return its
        RGB pixel data as a NumPy array."""
    try:
        if valid_format(path):
            img = Image.open(path).convert("RGB")
            arr = np.array(img)
            print(f"The shape of image is: {arr.shape}")
        return arr
    except Exception as x:
        print(x)

import numpy as np


def validation_arg(family: list, start: int, end: int) -> bool:
    """Validate the arguments of the slice_me function.

    Checks that family is a non-empty 2D structure and that
    start and end are integers.

    Args:
        family: A 2D list containing numerical values.
        start: The starting index of the slice.
        end: The ending index of the slice.

    Returns:
        True if all arguments are valid.

    Raises:
        ValueError: If family is empty, not 2D, or start/end
            are not integers.
    """
    arr_2d = np.array(family)
    if len(arr_2d) == 0:
        raise ValueError("The argument must not be empty.")
    if arr_2d.ndim != 2:
        raise ValueError("The arguments must be 2D.")
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("The start and end must be int")
    return True


def slice_me(family: list, start: int, end: int) -> list:
    """Slice a 2D list and display its shapes.

        Args:
            family: A 2D list containing numerical values.
            start: The starting index of the slice.
            end: The ending index of the slice.

        Returns:
            A sliced 2D list.
    """
    arr_2d = np.array(family)
    print("My shape is :", arr_2d.shape)
    res_arr = arr_2d[start:end]
    print("My new shape is :", res_arr.shape)
    return res_arr.tolist()


def main():
    """Run tests for the validation and slice_me functions."""
    family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
    try:
        validation_arg(family, 0, -2)
        validation_arg(family, 1, -2)
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except Exception as x:
        print(x)


if __name__ == "__main__":
    main()

import numpy as np

def valid_arg(height, weight):
    """Validate height and weight lists and raise errors for invalid arguments."""
    if len(height) != len(weight):
        raise ValueError("The lists must have the same length")
    if not all(isinstance(elem, (int, float)) for elem in height + weight):
        raise ValueError("The list should be int or float.")
    if len(height) == 0 and len(weight) == 0:
        raise ValueError("There should be arguments in the list.")
    if type(height) is not list or type(weight) is not list:
        raise TypeError("argument type: must be a list")
    return True

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """Calculate BMI values from height and weight lists."""
    try:
        if valid_arg(height, weight):
            h_arr = np.array(height)
            w_arr = np.array(weight)
            res = w_arr / (h_arr ** 2)
            return res.tolist()
    except Exception as x:
        print(x)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Check whether each BMI value is greater than the given limit."""
    bmi_arr = np.array(bmi)
    res_arr = bmi_arr > limit
    return res_arr.tolist()


def main():
    """Run the BMI calculation and display the results."""
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26)) 

if __name__ == "__main__":
    main()
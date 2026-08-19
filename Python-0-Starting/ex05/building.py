import sys


def main():
    """A function that counts the contents of a string."""
    upper = lower = space = digit = punctuation = 0
    try:
        if len(sys.argv) == 2:
            for i in sys.argv[1]:
                if i.isupper():
                    upper += 1
                elif i.islower():
                    lower += 1
                elif i.isspace():
                    space += 1
                elif i.isdigit():
                    digit += 1
                else:
                    punctuation += 1
            print(f"The text contains {len(sys.argv[1])} characters:")
            print(f"{upper} upper letters")
            print(f"{lower} lower letters")
            print(f"{punctuation} punctuation marks")
            print(f"{space} spaces")
            print(f"{digit} digits")
        elif len(sys.argv) > 2:
            raise AssertionError("Entering more than one!")
        else:
            print("Enter the argument.")
    except Exception as x:
        print(f"AssertionError: {x}")


if __name__ == "__main__":
    main()

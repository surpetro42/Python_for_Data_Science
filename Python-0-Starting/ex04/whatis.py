import sys

try:
    if len(sys.argv) == 2:
        try:
            arg = int((sys.argv[1]))
            if type(arg) == int:
                if arg % 2 == 0:
                    print("I'm Even.") 
                else:
                    print("I'm Odd.")
        except ValueError:
            raise AssertionError("argument is not an integer") 
    elif len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided") 
except Exception as x:
    print(f"AssertionError: {x}")

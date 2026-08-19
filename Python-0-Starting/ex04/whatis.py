import sys

try:
    if len(sys.argv) == 2:
        arg = int((sys.argv[1]))
        if type(arg) == int:
            if arg < 0:
                print("I'm Even.") 
            else:
                print("I'm Odd.")
    else:
        print("AssertionError: more than one argument is provided")
except:
    print("AssertionError: argument is not an integer")

def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: None {type(object)}")
    elif type(object) == float:
        print(f"Cheese: nan {type(object)}")
    elif type(object) == int:
        print(f"Zero: 0 {type(object)}")
    elif type(object) == str:
        print(f"Empty: {type(object)}")
    elif type(object) == bool:
        print(f"Fake: False {type(object)}")
    else:
        print("Type not Found")
        return 1
    return 0

# $>python tester.py | cat -e
# Nothing: None <class 'NoneType'>$
# Cheese: nan <class 'float'>$
# Zero: 0 <class 'int'>$
# Empty: <class 'str'>$
# Fake: False <class 'bool'>$
# Type not Found$
# 1$
# $>
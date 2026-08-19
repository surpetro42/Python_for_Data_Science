def all_thing_is_obj(object: any) -> int:
    if type(object) == list:
        print(f"List : {type(object)}")
    elif type(object) == tuple:
        print(f"Tuple : {type(object)}")
    elif type(object) == set:
        print(f"Set : {type(object)}")
    elif type(object) == dict:
        print(f"Dict : {type(object)}")
    elif object == "Brian":
        print(f"Brian is in the kitchen : {type(object)}")
    elif object == "Toto":
        print(f"Toto is in the kitchen : {type(object)}")
    else:
        print("Type not found")
    return 42

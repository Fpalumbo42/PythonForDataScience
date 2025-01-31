import math


def NULL_not_found(object: any) -> int:

    object_type = type(object)
    flag = 0

    if object is None:
        print(f"Nothing: {object} {object_type}")
    elif object_type == float and math.isnan(object):
        print(f"Cheese: {object} {object_type}")
    elif object_type == int and object == 0:
        print(f"Zero: {object} {object_type}")
    elif object_type == str and len(object) == 0:
        print(f"Empty: {object_type}")
    elif object_type == bool and object is False:
        print(f"Fake: {object} {object_type}")
    else:
        print("Type not Found")
        flag = 1

    return flag

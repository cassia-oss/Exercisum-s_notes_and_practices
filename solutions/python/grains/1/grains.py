def square(number):
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    else:
        return 2 ** (number-1)
    pass


def total():
    wheat_list = []
    for n in range(1,65):
        wheat_list.append(square(n))
    return sum(wheat_list)
    pass

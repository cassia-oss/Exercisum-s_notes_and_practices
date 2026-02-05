def square_root(number):
    add_step = 1
    L = 0
    while L * L < number:
        L = L + add_step
    return L
    pass

def square_root(number):
    lower = 0 
    higher = number
    while lower < higher:
        middle = (lower + higher) // 2
        if middle * middle < number:
            lower = middle +1
        else:
            higher = middle
    return lower
    pass

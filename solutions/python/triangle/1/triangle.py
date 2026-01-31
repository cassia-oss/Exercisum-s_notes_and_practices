def equilateral(sides):
    if sides[1] == sides[2] == sides[0] and sides[1] > 0:
        return True
    return False
    pass


def isosceles(sides):
    if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
        return False
    if not (sides[1] + sides[2] > sides[0] and (sides[1] + sides [0] > sides[2] and sides[2] + sides [0] > sides[1])):
        return False
    if sides[1] == sides[2] or (sides[1] == sides[0] or sides[2] == sides[0]):
        return True
    return False
    pass


def scalene(sides):
    if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
        return False
    if not (sides[1] + sides[2] > sides[0] and (sides[1] + sides [0] > sides[2] and sides[2] + sides [0] > sides[1])):
        return False
    if not (isosceles(sides) or equilateral(sides)) == True:
        return True
    return False
    pass

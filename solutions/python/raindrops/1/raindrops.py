def convert(number):
    s = ""
    if number % 3 == 0:
        s += "Pling"
    if number % 5 == 0:
        s += "Plang"
    if number % 7 == 0:
        s += "Plong"
    if not s:
        s = f"{number}"
    return s
    pass

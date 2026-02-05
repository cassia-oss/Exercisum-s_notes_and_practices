def find(search_list, value):
    lower_index = 0
    higher_index = len(search_list) - 1
    if higher_index == -1:
        raise ValueError("value not in array")
    while (higher_index - lower_index) > 0:
        middle_index = (lower_index + higher_index + 1) // 2
        if search_list[middle_index] > value:
            higher_index = middle_index - 1
        elif search_list[middle_index] == value:
            return middle_index
        else:
            lower_index = middle_index + 1
    if value == search_list[lower_index]:
        return lower_index
    else:
        raise ValueError("value not in array")
    pass

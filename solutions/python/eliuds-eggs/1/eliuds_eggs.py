def egg_count(display_value):
    binary_str = bin(display_value)[2:]
    display_value_list = list(binary_str)
    sum_eggs = 0
    for i in display_value_list:
        sum_eggs += int(i)
    return sum_eggs
    pass

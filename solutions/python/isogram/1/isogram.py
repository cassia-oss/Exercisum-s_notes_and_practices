def is_isogram(string):
    # 首先处理字符串，使其符合标准形式，这种形式是指：全部小写，并且不包括空格和‘-’
    temp_list = []
    for char in string:
        if char.isalpha():
            temp_list.append(char)
    classified_string_1 = ''.join(temp_list)
    classified_string_2 = classified_string_1.lower()
    # 接下来建立字典进行计数
    letter_count = {}  
    for letter in classified_string_2:
        if letter in letter_count:
            letter_count[letter] = letter_count[letter] + 1
        else:
            letter_count[letter] = 1
    # 进行判断
    for letter in classified_string_2:
        if letter_count[letter] > 1:
            return False
    return True
    pass

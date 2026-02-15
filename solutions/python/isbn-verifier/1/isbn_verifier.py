def is_valid(isbn):
    sum_list = 0
    #首先对isbn进行处理，使其变成能够方便计算的list形式
    isbn_1 = isbn.replace('-','')
    list_isbn = list(isbn_1)
    #检验
    #首先检验长度是否为10位
    if len(list_isbn) != 10:
        return False
    #检验是否只有最后一位为X，并且没有其他字符，并将其完全转化为int.格式的list
    for n in list_isbn:
        if n == 'X':
            if list_isbn.index(n) == 9:
                list_isbn[list_isbn.index(n)] = 10
            else:
                return False
        elif n.isalpha():
            return False
        else:
            list_isbn[list_isbn.index(n)] = int(n)
            
    for m in range(0,10):
        sum_list += list_isbn[m] * (10 - m)
    return sum_list % 11 == 0
    pass

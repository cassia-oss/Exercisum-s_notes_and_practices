def is_armstrong_number(number):
    # 步骤1：拆分每一位
    digits = [int(c) for c in str(abs(number))]
    # 步骤2：获取数字的位数（阿姆斯特朗数需要“位数次方”）
    n = len(digits)
    # 步骤3：计算每一位的n次方之和
    sum_pow = sum(d ** n for d in digits)
    # 步骤4：判断是否等于原数（兼容0和1，0和1都是阿姆斯特朗数）
    return sum_pow == abs(number)
    pass

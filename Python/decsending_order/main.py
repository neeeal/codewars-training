def descending_order(num):
    str_num = str(num)
    unique = sorted(set(str_num), reverse=True)
    result = ''
    for i in unique:
        result += i*str_num.count(i)
    return int(result)
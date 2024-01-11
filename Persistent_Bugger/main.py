def persistence(n):
    str_n = str(n)
    if len(str_n)<2:
        return 0
    times = 0
    while True:
        temp = 1
        for i in str_n:
            temp*=int(i)
        print(temp)
        times+=1
        if temp<10:
            return times
        str_n = str(temp)

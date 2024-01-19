def find_it(seq):
    for num in set(seq):
        temp=0
        for s in seq:
            if num==s: 
                temp+=1 
        if temp%2 == 1:
            return num
def first_non_repeating_letter(s):
    seen = dict()
    temp = s.lower()
    for x,i in enumerate(temp):
        if i not in seen: seen[i]=[0,x]
        if seen[i][0] < 2: seen[i][0] += 1
        if seen[i][0] == 2: del seen[i]
    if len(seen)==0: return ''
    return s[seen[next(iter(seen))][1]]
        
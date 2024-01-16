def sum_pairs(ints, s):
    smallest = len(ints)
    pair = None
#     for i in range(0,len(ints)-1):
#         for j in range(i+1,len(ints)):
#             if ints[i]+ints[j]==s and j<smallest:
#                 pair = [ints[i],ints[j]]
#                 smallest = j
    for i in range(len(ints)-1):
        if ints[i]+ints[i+1]==s and i+1<=smallest:
            pair = [ints[i],ints[i+1]]
            smallest = i+1
            print('found')
    print(pair)
    print(smallest)
    return pair
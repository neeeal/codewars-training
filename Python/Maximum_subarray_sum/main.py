def max_sequence(arr):
    if len(arr)==0 or all([x < 0 for x in arr]): return 0
    max_result = max(arr)
    for i in range(2,len(arr)+1):
        for j in range(i, len(arr)+1):
            if sum(arr[j-i:j]) > max_result:
                max_result = sum(arr[j-i:j])
                # print(arr[j-i:j])
    return max_result

# max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43])
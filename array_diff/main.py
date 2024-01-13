def array_diff(a, b):
    result = a.copy()
    for i in set(b):
        for j in a:
            if i==j: result.remove(i)
    return result
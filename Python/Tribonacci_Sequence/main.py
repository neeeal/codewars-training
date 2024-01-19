def tribonacci(signature, n):
    pass
    if n==0: return []
    elif n<3: return signature[:n]
    else:
        for i in range(3,n):
            signature.append(sum(signature[i-3:i]))
        return signature
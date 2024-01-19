def high_and_low(numbers):
    # ...
    numList = [int(x) for x in numbers.split()]
    result = f"{max(numList)} {min(numList)}"
    return result
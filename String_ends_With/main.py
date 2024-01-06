def solution(text, ending):
    # your code here...
    pass
    length = len(ending)
    result = False
    if length > len(text): pass
    if text[-length:] == ending: result = True
    return result
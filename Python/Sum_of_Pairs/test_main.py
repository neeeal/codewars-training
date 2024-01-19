from main import sum_pairs
l1 = [1, 4, 8, 7, 3, 15]
l2 = [1, -2, 3, 0, -6, 1]
l3 = [20, -13, 40]
l4 = [1, 2, 3, 4, 1, 0]
l5 = [10, 5, 2, 3, 7, 5]
l6 = [4, -2, 3, 3, 4]
l7 = [0, 2, 0]
l8 = [5, 9, 13, -3]
l9 = [1] * 10000000
l9[len(l9) // 2 - 1] = 6
l9[len(l9) // 2] = 7
l9[len(l9) - 2] = 8
l9[len(l9) - 1] = -3
l9[0] = 13
l9[1] = 3

def test_1():
    assert(sum_pairs(l1, 8) == [1, 7])
def test_2():
    assert(sum_pairs(l2, -6) == [0, -6])
def test_3():
    assert(sum_pairs(l3, -7) == None)
def test_4():
    assert(sum_pairs(l4, 2) == [1, 1])
def test_5():
    assert(sum_pairs(l5, 10) == [3, 7])
def test_6():
    assert(sum_pairs(l6, 8) == [4, 4])
def test_7():
    assert(sum_pairs(l7, 0) == [0, 0])
def test_8():
    assert(sum_pairs(l8, 10) == [13, -3])
def test_9():
    assert(sum_pairs(l9, 13) == [6, 7])
def test_10():
    assert(sum_pairs(l9, 5) == [8, -3])
def test_11():
    assert(sum_pairs(l9, 16) == [13, 3])
def test_12():
    assert(sum_pairs(l9, 31) == None)


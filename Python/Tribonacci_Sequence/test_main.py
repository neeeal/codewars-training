from main import tribonacci
def test_1():
    sample = ([1, 1, 1], 10)
    assert(tribonacci(sample[0],sample[1])) == [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
def test_2():
    sample = ([0, 0, 1], 10)
    assert(tribonacci(sample[0],sample[1])) == [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
def test_3():
    sample = ([0, 1, 1], 10)
    assert(tribonacci(sample[0],sample[1])) == [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]
def test_4():
    sample = ([1, 0, 0], 10)
    assert(tribonacci(sample[0],sample[1])) == [1, 0, 0, 1, 1, 2, 4, 7, 13, 24]
def test_5():
    sample = ([0, 0, 0], 10)
    assert(tribonacci(sample[0],sample[1])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def test_6():
    sample = ([1, 2, 3], 10)
    assert(tribonacci(sample[0],sample[1])) == [1, 2, 3, 6, 11, 20, 37, 68, 125, 230]
def test_7():
    sample = ([3, 2, 1], 10)
    assert(tribonacci(sample[0],sample[1])) == [3, 2, 1, 6, 9, 16, 31, 56, 103, 190]
def test_8():
    sample = ([1, 1, 1], 1)
    assert(tribonacci(sample[0],sample[1])) == [1]
def test_9():
    sample = ([300, 200, 100], 0)
    assert(tribonacci(sample[0],sample[1])) == []
def test_10():
    sample = ([0, 0, 1], 10)
    assert(tribonacci(sample[0],sample[1])) == [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
def test_11():
    sample = ([0.5, 0.5, 0.5], 30)
    assert(tribonacci(sample[0],sample[1])) == [0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5, 96.5, 177.5, 326.5, 600.5, 1104.5, 2031.5, 3736.5, 6872.5, 12640.5, 23249.5, 42762.5, 78652.5, 144664.5, 266079.5, 489396.5, 900140.5, 1655616.5, 3045153.5, 5600910.5, 10301680.5]
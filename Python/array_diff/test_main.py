from main import array_diff
def test_1():
    sample = ([1,2], [1])
    assert(array_diff(sample[0],sample[1])) == [2]
def test_2():
    sample = ([1,2,2], [1])
    assert(array_diff(sample[0],sample[1])) == [2,2]
def test_3():
    sample = ([1,2,2], [2])
    assert(array_diff(sample[0],sample[1])) == [1]
def test_4():
    sample = ([1,2,2], [])
    assert(array_diff(sample[0],sample[1])) == [1,2,2]
def test_5():
    sample = ([], [1,2])
    assert(array_diff(sample[0],sample[1])) == []
def test_6():
    sample = ([1,2,3], [1, 2])
    assert(array_diff(sample[0],sample[1])) == [3]
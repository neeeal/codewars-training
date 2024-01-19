from main import count_by
def test_1():
    sample = (1,5)
    assert(count_by(sample[0],sample[1])) == [1, 2, 3, 4, 5]
def test_2():
    sample = (2,5)
    assert(count_by(sample[0],sample[1])) == [2, 4, 6, 8, 10]
def test_3():
    sample = (3,5)
    assert(count_by(sample[0],sample[1])) == [3, 6, 9, 12, 15]
def test_4():
    sample = (50,5)
    assert(count_by(sample[0],sample[1])) == [50, 100, 150, 200, 250]
def test_5():
    sample = (100,5)
    assert(count_by(sample[0],sample[1])) == [100, 200, 300, 400, 500]
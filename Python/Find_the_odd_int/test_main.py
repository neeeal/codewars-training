from main import find_it
def test_1():
    sample = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]

    assert(find_it(sample)) == 5
def test_2():
    sample = [1,1,2,-2,5,2,4,4,-1,-2,5]
    assert(find_it(sample)) == -1
def test_3():
    sample = [20,1,1,2,2,3,3,5,5,4,20,4,5]
    assert(find_it(sample)) == 5
def test_4():
    sample = [10]
    assert(find_it(sample)) == 10
def test_5():
    sample = [10, 10, 10]
    assert(find_it(sample)) == 10
def test_6():
    sample = [1,1,1,1,1,1,10,1,1,1,1]
    assert(find_it(sample)) == 10
def test_7():
    sample = [5,4,3,2,1,5,4,3,2,10,10]
    assert(find_it(sample)) == 1
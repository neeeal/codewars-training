from main import square_sum
def test_1():
    sample = [1,2]
    assert(square_sum(sample)) == 5 
def test_2():
    sample = [0,3,4,5]
    assert(square_sum(sample)) == 50 
def test_3():
    sample = []
    assert(square_sum(sample)) == 0
def test_4():
    sample = [-1,-2]
    assert(square_sum(sample)) == 5 
def test_5():
    sample = [-1,0,1]
    assert(square_sum(sample)) == 2
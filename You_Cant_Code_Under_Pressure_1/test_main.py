from main import double_integer
def test_1():
    sample = 2
    assert(double_integer(sample)) == 4
def test_2():
    sample = 4
    assert(double_integer(sample)) == 8 
def test_3():
    sample = -10
    assert(double_integer(sample)) == -20
def test_4():
    sample = 0
    assert(double_integer(sample)) == 0
def test_5():
    sample = 100
    assert(double_integer(sample)) == 200
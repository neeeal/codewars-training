from main import max_sequence
def test_1():
    sample = []
    assert(max_sequence(sample)) == 0
def test_2():
    sample = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert(max_sequence(sample)) == 6
def test_3():
    sample = [-2, -1, -3, -4, -1, -2, -1, -5, -4]
    assert(max_sequence(sample)) == 0
def test_4():
    sample = [7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]
    assert(max_sequence(sample)) == 155
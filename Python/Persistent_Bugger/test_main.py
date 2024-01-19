from main import persistence
def test_1():
    sample = 39
    assert(persistence(sample)) == 3
def test_2():
    sample = 4
    assert(persistence(sample)) == 0
def test_3():
    sample = 25
    assert(persistence(sample)) == 2
def test_4():
    sample = 999
    assert(persistence(sample)) == 4
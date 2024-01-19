from main import high_and_low
def test_1():
    sample = "8 3 -5 42 -1 0 0 -9 4 7 4 -4"
    assert(high_and_low(sample)) == "42 -9"
def test_2():
    sample = "1 2 3"
    assert(high_and_low(sample)) == "3 1"
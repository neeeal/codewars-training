from main import ips_between
def test_1():
    assert(ips_between(0)== 0)
def test_2():
    assert(ips_between(15)== 51)
def test_2():
    assert(ips_between(123456789)== 987654321)

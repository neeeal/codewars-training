from main import ips_between
def test_1():
    assert(ips_between("10.0.0.0", "10.0.0.50")== 50)
def test_2():
    assert(ips_between("20.0.0.10", "20.0.1.0")== 246)

from main import make_readable
def test_1():
    assert(make_readable(0) == "00:00:00")
def test_2():
    assert(make_readable(59) == "00:00:59")
def test_3():
    assert(make_readable(60) == "00:01:00")
def test_4():
    assert(make_readable(3599) == "00:59:59")
def test_5():
    assert(make_readable(3600) == "01:00:00")
def test_6():
    assert(make_readable(86399) == "23:59:59")
def test_7():
    assert(make_readable(86400) == "24:00:00")
def test_8():
    assert(make_readable(359999) == "99:59:59")
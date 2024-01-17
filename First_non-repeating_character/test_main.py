from main import first_non_repeating_letter
def test_1():
    assert(first_non_repeating_letter('a') == 'a')
def test_2():
    assert(first_non_repeating_letter('stress') == 't')
def test_3():
    assert(first_non_repeating_letter('moonmen') == 'e')
def test_4():
    assert(first_non_repeating_letter('') == '')
def test_5():
    assert(first_non_repeating_letter('abba') == '')
def test_6():
    assert(first_non_repeating_letter('aa') == '')
def test_7():
    assert(first_non_repeating_letter('~><#~><') == '#')
def test_8():
    assert(first_non_repeating_letter('hello world, eh?') == 'w')
def test_9():
    assert(first_non_repeating_letter('sTreSS') == 'T')
def test_10():
    assert(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!') == ',')
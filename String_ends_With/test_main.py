from main import solution
def test_1():
    sample = ( "samurai", "ai"    )
    assert(solution(sample[0],sample[1])) == True
def test_2():
    sample = ( "ninja",   "ja"    )
    assert(solution(sample[0],sample[1])) == True
def test_3():
    sample = ( "sensei",  "i"     )
    assert(solution(sample[0],sample[1])) == True
def test_4():
    sample = ( "abc",     "abc"   )
    assert(solution(sample[0],sample[1])) == True
def test_5():
    sample = ( "abcabc",  "bc"    )
    assert(solution(sample[0],sample[1])) == True
def test_6():
    sample = ( "fails",   "ails"  )
    assert(solution(sample[0],sample[1])) == True
def test_7():
    sample = ( "sumo",    "omo"   )
    assert(solution(sample[0],sample[1])) == False
def test_8():
    sample = ( "samurai", "ra"    )
    assert(solution(sample[0],sample[1])) == False
def test_9():
    sample = ( "abc",     "abcd"  )
    assert(solution(sample[0],sample[1])) == False
def test_10():
    sample = ( "ails",    "fails" )
    assert(solution(sample[0],sample[1])) == False
def test_12():
    sample = ( "this",    "fails" )
    assert(solution(sample[0],sample[1])) == False
def test_12():
    sample = ( "spam",    "eggs"  )
    assert(solution(sample[0],sample[1])) == False

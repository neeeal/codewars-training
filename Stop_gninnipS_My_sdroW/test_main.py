from main import spin_words
def test_1():
    sample = "Welcome"
    assert(spin_words(sample)) == "emocleW"
def test_2():
    sample = "to"
    assert(spin_words(sample)) == "to"
def test_3():
    sample = "CodeWars"
    assert(spin_words(sample)) == "sraWedoC"
def test_4():
    sample = "Hey fellow warriors"
    assert(spin_words(sample)) == "Hey wollef sroirraw"
def test_5():
    sample = "This sentence is a sentence"
    assert(spin_words(sample)) == "This ecnetnes is a ecnetnes"
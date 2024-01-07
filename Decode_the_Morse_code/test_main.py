from main import decode_morse
def test_1():
    sample = '.... . -.--   .--- ..- -.. .'
    assert(decode_morse(sample)) == 'HEY JUDE'
def test_2():
    sample = '.-'
    assert(decode_morse(sample)) == 'A'
def test_3():
    sample = '--...'
    assert(decode_morse(sample)) == '7'
def test_4():
    sample = '...-..-'
    assert(decode_morse(sample)) == '$'
def test_5():
    sample = '.'
    assert(decode_morse(sample)) == 'E'
def test_6():
    sample = '..'
    assert(decode_morse(sample)) == 'I'
def test_7():
    sample = '. .'
    assert(decode_morse(sample)) == 'E E'
def test_8():
    sample = '...-..- ...-..- ...-..-'
    assert(decode_morse(sample)) == '$$$'
def test_9():
    sample = '----- .---- ..--- ---.. ----.'
    assert(decode_morse(sample)) == '01289'
def test_10():
    sample = '.-... ---...   -..-. --...'
    assert(decode_morse(sample)) == '&: /7'
def test_11():
    sample = '...---...'
    assert(decode_morse(sample)) == 'SOS'
def test_12():
    sample = '... --- ...'
    assert(decode_morse(sample)) == 'SOS'
def test_13():
    sample = '...   ---   ...'
    assert(decode_morse(sample)) == 'S O S'
def test_14():
    sample = ' . '
    assert(decode_morse(sample)) == 'E'
def test_15():
    sample = '   .   . '
    assert(decode_morse(sample)) == 'E E'
def test_16():
    sample = '      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '
    assert(decode_morse(sample)) == 'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.'
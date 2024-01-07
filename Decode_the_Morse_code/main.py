from preloaded import MORSE_CODE

def decode_morse(morse_code):
    # Remember - you can use the preloaded MORSE_CODE dictionary:
    # For example: 
    # MORSE_CODE['.-'] = 'A'
    # MORSE_CODE['--...'] = '7'
    # MORSE_CODE['...-..-'] = '$'
    pass
    sentence = morse_code.strip().split("   ")
    words = [word.split() for word in sentence]
    message = ' '.join([''.join([MORSE_CODE[letter] for letter in word]) for word in words])
    return message

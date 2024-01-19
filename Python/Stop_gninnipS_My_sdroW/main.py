def spin_words(sentence):
    # Your code goes here
    return ' '.join([word if len(word)<5 else word[::-1] for word in sentence.split()])
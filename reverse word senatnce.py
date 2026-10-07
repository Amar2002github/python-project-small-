

def reverse_words(sentence):
    words = sentence.split()

    words.reverse()

    return ' '.join(words)


print(reverse_words("I learn  Python"))
print(reverse_words("I learn  JavaScript"))
all_26_letters = 'abcdefghijklmnopqrstuvwxyz'
def is_pangram(sentence):
    lower_sentence = sentence.lower()
    for letter in all_26_letters: 
        if letter not in lower_sentence:
            return False
    return True
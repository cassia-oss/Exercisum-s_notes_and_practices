def response(hey_bob):
    hey_bob = hey_bob.rstrip()
    if len(hey_bob) == 0:
        return "Fine. Be that way!"
    elif hey_bob[-1] == '?' and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    elif hey_bob[-1] == '?':
        return "Sure."
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    elif not any(char.isalpha() for char in hey_bob) and not any(char.isdigit() for char in hey_bob):
        return "Fine. Be that way!"
    return "Whatever."
    pass

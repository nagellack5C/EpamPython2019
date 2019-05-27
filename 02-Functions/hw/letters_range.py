def letters_range(*args, **kwargs):
    '''
    Returns alphabet range when given letters. Given one letter returns
    alphabet slice from 'a' to this letter; given two letters returns
    slice from first to second letter. If an int is given as a third
    argument it is interpreted as step. Kwargs interpreted as a
    translation table.
    :param args: stop (str) / start (str), stop (str) / start (str),
    stop (str), step (int)
    :param kwargs: translation table ({str: replacement})
    :return: alphabet slice according to the args given
    '''
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    if kwargs:
        # first I scan kwargs and store letter indices to prevent double
        # replacements (e.g. if kwargs == {"a": "z", "z": "a"} then
        # if we scan and replace keys 1 by 1 we'd get 'a...a' alphabet
        # instead of 'z...a' alphabet as intended)
        replacements = []
        for char in kwargs:
            replacements.append((alphabet.index(char), str(kwargs[char])))
        for rep in replacements:
            alphabet[rep[0]] = rep[1]
    if len(args) == 1:
        stop = alphabet.index(args[0])
        return alphabet[:stop]
    if len(args) == 2:
        start = alphabet.index(args[0])
        stop = alphabet.index(args[1])
        step = -1 if start > stop else 1
        return alphabet[start:stop:step]
    if len(args) == 3:
        start = alphabet.index(args[0])
        stop = alphabet.index(args[1])
        step = args[2]
        return alphabet[start:stop:step]

print(letters_range("b"))
print(letters_range("b", "j"))
print(letters_range("b", "j", 2))
print(letters_range("j", "b", **{'l': 7, 'o': 0}))
print(letters_range("k", "z", **{'l': 7, 'o': 0}))

def test(**kwargs):
    print(kwargs)

print([i for i in range(10, -1)])
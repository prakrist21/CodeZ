MIN = 97
MAX = 122

def encode_char(a):
    if not a.islower():
        return a                    # return as-is if not a-z
    new_value = ord(a) + 6
    if new_value > MAX:
        diff = new_value - MAX - 1
        new_value = MIN + diff
    return chr(new_value)

def decode_char(a):
    if not a.islower():
        return a                    # return as-is if not a-z
    new_value = ord(a) - 6
    if new_value < MIN:
        diff = MIN - new_value - 1
        new_value = MAX - diff
    return chr(new_value)

def encode_sentence(sent):
    sent = rev_sentence(sent)
    result = ""
    for x in sent:
        if x == " ":
            result += " "
        elif x.isupper():
            result += encode_char(x.lower()).upper()   # handle uppercase
        else:
            result += encode_char(x)
    return result

def decode_sentence(sent):
    result = ""
    for x in sent:
        if x == " ":
            result += " "
        elif x.isupper():
            result += decode_char(x.lower()).upper()   # handle uppercase
        else:
            result += decode_char(x)
    result = rev_sentence(result)
    return result

def rev_sentence(sent):
    words = sent.split(" ")
    return " ".join(word[::-1] for word in words)
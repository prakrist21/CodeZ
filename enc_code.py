MIN = 97
MAX = 122

# --- CodeZ (original) ---

def encode_char(a):
    if not a.islower():
        return a
    new_value = ord(a) + 6
    if new_value > MAX:
        diff = new_value - MAX - 1
        new_value = MIN + diff
    return chr(new_value)

def decode_char(a):
    if not a.islower():
        return a
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
            result += encode_char(x.lower()).upper()
        else:
            result += encode_char(x)
    return result

def decode_sentence(sent):
    result = ""
    for x in sent:
        if x == " ":
            result += " "
        elif x.isupper():
            result += decode_char(x.lower()).upper()
        else:
            result += decode_char(x)
    result = rev_sentence(result)
    return result

def rev_sentence(sent):
    words = sent.split(" ")
    return " ".join(word[::-1] for word in words)


# --- Reverse Only ---

def reverse_encode(sent):
    return rev_sentence(sent)

def reverse_decode(sent):
    return rev_sentence(sent)


# --- Binary ---

def binary_encode(sent):
    return " ".join(format(ord(c), '08b') for c in sent)

def binary_decode(sent):
    try:
        bits = sent.strip().split(" ")
        return "".join(chr(int(b, 2)) for b in bits)
    except:
        return "Invalid binary input"
    
# --- Atbash ---

def atbash_encode(sent):
    result = ""
    for x in sent:
        if x.isalpha():
            if x.isupper():
                result += chr(ord('Z') - (ord(x) - ord('A')))
            else:
                result += chr(ord('z') - (ord(x) - ord('a')))
        else:
            result += x
    return result

def atbash_decode(sent):
    return atbash_encode(sent)  # atbash is its own inverse


# --- Morse Code ---

MORSE_MAP = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}
REVERSE_MORSE = {v: k for k, v in MORSE_MAP.items()}

def morse_encode(sent):
    result = []
    for x in sent.upper():
        if x == ' ':
            result.append('/')
        elif x in MORSE_MAP:
            result.append(MORSE_MAP[x])
        else:
            result.append(x)
    return ' '.join(result)

def morse_decode(sent):
    result = ""
    words = sent.strip().split(' / ')
    for word in words:
        letters = word.strip().split(' ')
        for letter in letters:
            if letter in REVERSE_MORSE:
                result += REVERSE_MORSE[letter]
            elif letter:
                result += letter
        result += ' '
    return result.strip()


# --- Rail Fence ---

def rail_fence_encode(sent, rails=3):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    for char in sent:
        fence[rail].append(char)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction
    return ''.join(''.join(r) for r in fence)

def rail_fence_decode(sent, rails=3):
    n = len(sent)
    pattern = []
    rail = 0
    direction = 1
    for i in range(n):
        pattern.append(rail)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction

    indices = sorted(range(n), key=lambda i: pattern[i])
    result = [''] * n
    for i, char in zip(indices, sent):
        result[i] = char
    return ''.join(result)


# --- ASCII Shift ---

def ascii_encode(sent, shift=10):
    return ' '.join(str(ord(c) + shift) for c in sent)

def ascii_decode(sent, shift=10):
    try:
        return ''.join(chr(int(x) - shift) for x in sent.strip().split(' '))
    except:
        return "Invalid ASCII input"
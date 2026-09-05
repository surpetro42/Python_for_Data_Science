import sys

morse = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',

    ' ': '/'
}


def encoding(string, morse):
    """Encode a string into Morse code and print the result."""
    string = string.upper()
    morse_code = []
    for char in string:
        morse_code.append(morse[char])
    print(" ".join(morse_code))


def valid_input(s):
    """Check if a string contains only alphanumeric characters and spaces."""
    if all(c.isalnum() or c == " " for c in s):
        return True
    return False


def main():
    """The function receives a string and returns it in Morse code"""
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        if valid_input(sys.argv[1]) is False:
            raise AssertionError("the arguments are bad")
        encoding(sys.argv[1], morse)
    except AssertionError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()

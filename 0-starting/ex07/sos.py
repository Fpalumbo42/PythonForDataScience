import sys

NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def main():
    '''
    Main function that checks the arguments and prints\
    the morse code of the input
    Argument is a string of characters
    '''
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        for c in sys.argv[1]:
            if c.upper() not in NESTED_MORSE:
                raise AssertionError("the arguments are bad")
        print(' '.join([NESTED_MORSE[c.upper()] for c in sys.argv[1]]))

    except AssertionError as error:
        print(f"{type(error).__name__}: {error}")
        exit(1)


if __name__ == "__main__":
    main()

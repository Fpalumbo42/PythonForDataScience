import sys


def check_str(str):

    '''
    Count and print the number of upper and lower letters,
    punctuation marks, spaces and digits in a string
    '''

    counts = {
        "upper": 0,
        "lower": 0,
        "ponctuation": 0,
        "spaces": 0,
        "digits": 0
    }

    punctuation_characters = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    for char in str:
        if char.isupper():
            counts["upper"] += 1
        if char.islower():
            counts["lower"] += 1
        if char in punctuation_characters:
            counts["ponctuation"] += 1
        if char.isspace():
            counts["spaces"] += 1
        if char.isdigit():
            counts["digits"] += 1

    print(f"The text contains {len(str)} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['ponctuation']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")


def main():
    '''
    Take a string as input and count the number of upper and lower letters,
    punctuation marks, spaces and digits
    '''
    try:
        if len(sys.argv) < 2:
            try:
                print("What is the text to count?\n")
                str = sys.stdin.readline()
            except EOFError:
                pass
        elif len(sys.argv) == 2:
            str = sys.argv[1]
        else:
            raise AssertionError("Too many arguments provided")
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        exit(1)
    check_str(str)

    # Permet de lancer le programme si il n'est pas importé
    if __name__ == "__main__":
        main()

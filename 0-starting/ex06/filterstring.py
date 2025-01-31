import sys
from ft_filter import ft_filter


def main():
    '''
    Main function that filters words based on their length
    take a string and an int as arguments
    print list of words that are longer than the int
    '''
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        if not all(c.isalpha() or c == ' ' for c in sys.argv[1]):
            raise AssertionError("the first argument \
                                 must only contain letters and spaces")
        if int(sys.argv[2]) <= 0:
            raise AssertionError("the int must be positive")

    except (ValueError, TypeError):
        print("AssertionError: the second argument must be a positive integer")
        exit(1)

    except AssertionError as error:
        print(f"{type(error).__name__}: {error}")
        exit(1)

    words = sys.argv[1].split()

    print(list(ft_filter(lambda x: len(x) > int(sys.argv[2]), words)))


if __name__ == "__main__":
    main()

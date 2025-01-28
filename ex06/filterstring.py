import sys
def 
def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        if sys.argv[2] is not int:
            raise AssertionError("the argumfsfents are bad")
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        exit(1)

if __name__ == "__main__":
    main()
def main():
    print(True == 1)
    print('' == 1)
    print([] == 1)
    print(10 == 10.0)
    print(str([] == []) + '\n')

    # "is" compares memory location
    print([] is [])
    # Produces warning: "SyntaxWarning: "is" with a literal"
    print(True is 1)
    print('' is 1)
    print([] is 1)
    print(10 is 10.0)


if __name__ == '__main__':
    main()

def main():
    # Walrus operator lets you assign variables as part of a larger expression
    a = input('Input a string: ')
    if (n := len(a)) > 10:
        print(f"String is too long.\nLength of {n}.")


if __name__ == '__main__':
    main()

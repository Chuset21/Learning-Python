def main():
    try:
        with open('test.txt', mode='r+') as my_file:
            n = my_file.write('Hey, it\'s me')    # Returns the number of chars written
            print(n)

            # my_file.seek(0)
            # print(my_file.readline())
            # print(my_file.readlines())
    except (FileNotFoundError, IOError) as err:
        print(err)


if __name__ == '__main__':
    main()

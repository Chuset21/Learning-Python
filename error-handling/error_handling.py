def div(x, y):
    try:
        return x / y
    except (TypeError, ZeroDivisionError) as err:
        print(err)


def main():
    while True:
        try:
            age = int(input('What is your age? '))
            print(age)
            # Raising errors:
            # raise ZeroDivisionError('Hey cut it out')
        except ValueError:
            print('Please enter a number')
        else:
            break
        finally:
            print('finally')

    print(div(1, '2'))


if __name__ == '__main__':
    main()

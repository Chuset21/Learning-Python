def main():
    print(type(6))
    print(type(2 / 4))
    print(type(int(2.2)))
    print(2 ** 3)
    print(7 // 4.1)   # Floor division
    print(5 % 4)

    print(round(3.1))
    print(round(3.9))
    print(abs(-3))

    print(bin(5).replace('0b', ''))

    # '0b' optional in this expression
    print(int('0b101', 2))
    # print(int('101', 2))

    long_string = '''You
can
do
multi-line
strings'''
    print(f'\nlong_string:\n{long_string}\n')

    formatted_string = 'Hi {}. You are {} years old'.format('John', 55)
    print(formatted_string)
    formatted_string = 'Hi {1}. You are {0} years old'.format(56, 'Susan')
    print(formatted_string)

    s = '01234567'
    # [start:stop:step]
    print(s[0], s[0:3], s[0:7:2], s[1:], s[:5], s[::3], s[-2], s[::-1])

    print(len(s))


if __name__ == '__main__':
    main()

def fibonacci(index):
    a = 0
    b = 1
    for i in range(index):
        yield a
        temp = a
        a = b
        b += temp


def main():
    for i in fibonacci(20):
        print(i)


if __name__ == '__main__':
    main()

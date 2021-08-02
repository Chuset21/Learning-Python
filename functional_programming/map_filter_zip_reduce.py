from functools import reduce


def main():
    my_tuple = (1, 2, 3, 4, 5, 6)
    your_tuple = tuple(map(lambda p: p * 2, my_tuple))

    print(your_tuple)

    print(tuple(filter(lambda p: p % 2 != 0, my_tuple)))

    print(tuple(zip(my_tuple, your_tuple)))

    print((reduce(lambda acc, p: acc + p, my_tuple, 0)))


if __name__ == '__main__':
    main()

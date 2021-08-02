from functools import reduce


def mul_2(item):
    return item * 2


def is_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    return acc + item


def main():
    my_tuple = (1, 2, 3, 4, 5, 6)
    your_tuple = tuple(map(mul_2, my_tuple))

    print(your_tuple)

    print(tuple(filter(is_odd, my_tuple)))

    print(tuple(zip(my_tuple, your_tuple)))

    print((reduce(accumulator, my_tuple, 0)))


if __name__ == '__main__':
    main()

from functools import reduce


def main():
    my_tuple = (1, 2, 3, 4, 5, 6)
    your_tuple = tuple(map(lambda p: p * 2, my_tuple))

    print(your_tuple)

    print(tuple(filter(lambda p: p % 2 != 0, my_tuple)))

    print(tuple(zip(my_tuple, your_tuple)))

    print((reduce(lambda acc, p: acc + p, my_tuple, 0)))

    # List Sorting
    a = [(0, 2), (4, 3), (10, -1), (9, 9)]
    a.sort(key=lambda p: p[1])
    print(a)


if __name__ == '__main__':
    main()

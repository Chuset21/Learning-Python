def main():
    # immutable
    my_tuple = (1, 2, 3, 4, 5)
    print(my_tuple)
    print(5 in my_tuple)

    new_tuple = my_tuple[1:2]
    print(new_tuple)

    x, y, z, *other = my_tuple
    print(x, y, z, other)

    print(my_tuple.count(5))
    print(my_tuple.index(5))
    print(len(my_tuple))


if __name__ == '__main__':
    main()

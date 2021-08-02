def main():
    my_list = [char for char in 'hello']
    my_tuple = tuple(char for char in 'hello')

    print(my_list)
    print(my_tuple)

    my_list2 = [num * 2 for num in range(11)]
    print(my_list2)

    my_list3 = [num ** 2 for num in range(21) if num % 2 == 0]
    print(my_list3)

    # Set comprehension
    my_set = {char for char in 'hello'}
    print(my_set)

    # Dictionary comprehension
    my_dict = {key: value ** 2 for key, value in {'a': 1, 'b': 2, 'c': 3, 'd': 4}.items()}
    print(my_dict)

    my_dict2 = {num: num * 2 for num in range(1, 11)}
    print(my_dict2)


if __name__ == '__main__':
    main()

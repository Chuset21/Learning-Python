# Similar to hashmaps
def main():
    # Keys must be of immutable types
    dictionary = {
        'a': 1,
        'b': 2
    }
    print(dictionary)
    print(dictionary.get('b'))
    # Default value with #get
    print(dictionary.get('d', 55))

    print(list(dictionary.keys()))

    print('a' in dictionary)
    print(1 in dictionary.values())

    # Returns tuples
    print(dictionary.items())

    dictionary.update({'a': 3, 'c': 45})
    print(dictionary.pop('a'))
    print(dictionary)


if __name__ == '__main__':
    main()

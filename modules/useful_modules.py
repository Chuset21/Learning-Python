from collections import Counter, defaultdict
import datetime
from array import array


def is_dict_order_equal(dict1: dict, dict2: dict):
    return tuple(dict1.items()) == tuple(dict2.items())


def main():
    li = [1, 2, 3, 4, 5, 6, 7, 7]
    sentence = 'blah blah blah thinking about python'
    print(Counter(li))
    print(Counter(sentence))

    dictionary = defaultdict(lambda: 5, {'a': 1, 'b': 2})
    print(dictionary.get('c'))  # None
    print(dictionary['c'])  # 5

    ordered_dict = {'c': 3, 'a': 1, 'b': 2}
    ordered_dict2 = {'c': 3, 'b': 2, 'a': 1}
    print(ordered_dict == ordered_dict2)  # True, doesn't check order
    # Since python3.8: dictionaries (the dict type) are ordered by default.
    print(is_dict_order_equal(ordered_dict, ordered_dict2))  # False, checks order

    print(datetime.time(5, 45, 2))
    print(datetime.date.today())

    arr = array('i', [1, 2, 3])  # typecode: 'i' for signed ints
    print(arr[0])
    arr.append(4)
    print(arr)


if __name__ == '__main__':
    main()

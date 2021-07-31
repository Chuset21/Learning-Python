def main():
    my_set = {1, 2, 3, 4, 5}
    my_set.add(6)
    your_set = {4, 5, 6, 7, 8, 9, 10}

    print(my_set)
    print(1 in my_set)
    print(len(my_set))

    print(my_set.difference(your_set))
    print(your_set.difference(my_set))

    my_set.discard(6)
    print(my_set)

    a_set = my_set.copy()
    a_set.difference_update(your_set)
    print(a_set)

    print(my_set.intersection(your_set))
    # Same thing
    print(my_set & your_set)

    # Returns True if sets have no common elements
    print(my_set.isdisjoint(your_set))

    print(my_set.union(your_set))
    # Same thing
    print(my_set | your_set)

    a_set = my_set.intersection(your_set)
    print(a_set.issubset(your_set))

    print(your_set.issuperset(a_set))


if __name__ == '__main__':
    main()

def main():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8]
    print(list1[-1])

    print(list1[0::2])
    # Making a copy of a list, instead of the reference
    list2 = list1[:]
    list2.append(100)
    list2.extend([100, 101])
    print(list2)
    print(list2.pop())
    list2.remove(100)
    print(list2)

    basket = sorted(['a', 'b', 'c', 'd', 'e', 'd'])
    # basket.sort()
    print(basket.index('d'))
    print('d' in basket)
    print(basket.count('d'))
    basket.reverse()
    print(basket[::-1])

    print(list(range(10)))

    print(' '.join(['Hi', 'my', 'name', 'is', 'Jojo']))

    # list unpacking
    a, b, c, *other, d = list1
    print(a)
    print(b)
    print(c)
    print(other)
    print(d)


if __name__ == '__main__':
    main()

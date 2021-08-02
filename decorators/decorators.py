def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('***')
        func(*args, **kwargs)
        print('***')

    return wrap_func


@my_decorator
def greet(greeting, emoji=':('):
    print(greeting, emoji)


@my_decorator
def bye():
    print('bye')


def main():
    greet('hello')
    print()
    bye()


if __name__ == '__main__':
    main()

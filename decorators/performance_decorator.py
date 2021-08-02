from time import time


def performance(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        print(f'Took {time() - t1} seconds')
        return result

    return wrap_func


@performance
def long_time():
    return [i / 5.6 * 2.311 for i in range(100000000)]


def main():
    my_list = long_time()


if __name__ == '__main__':
    main()

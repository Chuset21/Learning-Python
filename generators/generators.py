class MyGenerator:
    def __init__(self, start, stop, step=1):
        self._start = start
        self._stop = stop
        self._step = step
        self._current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self._has_remaining_iterations():
            num = self._current
            self._iterate_current()
            return num
        raise StopIteration

    def _iterate_current(self):
        self._current += self._step

    def _has_remaining_iterations(self):
        return (self._current < self._stop) if self._step > 0 else (self._stop < self._current)


def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
            print(iterator)
        except StopIteration:
            break


def generator_function(n: int):
    for i in range(n):
        yield i


def make_list(n: int):
    return [i * 2 for i in range(n)]


def main():
    # range() is a generator
    my_list = make_list(10)
    print(my_list)

    for i in generator_function(10):
        print(i)

    g = generator_function(10)
    print(g)
    print(next(g))
    print(next(g))

    print()
    special_for([1, 2, 3])
    print()

    gen = MyGenerator(50, 0, -2)
    for i in gen:
        print(i)


if __name__ == '__main__':
    main()

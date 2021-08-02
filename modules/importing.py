from decorators.performance_decorator import performance
from generators.generators import MyGenerator as Gen, generator_function as gen_func


@performance
def main():
    for i in gen_func(2):
        print(i)

    print()

    for i in Gen(0, 10):
        print(i)


if __name__ == '__main__':
    main()

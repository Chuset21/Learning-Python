# Converts *args to tuple and **kwargs to a dict (with the variable names given stringified
# Parameter order rule: params, *args, default parameters, **kwargs
def super_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


def main():
    print(super_sum(1, 2, 3, 4, 5, num1=5, num2=10))


if __name__ == '__main__':
    main()

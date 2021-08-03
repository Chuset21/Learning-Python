import re


def main():
    pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-z0-9-]+\.[a-zA-Z0-9-.]+$)")
    email = 'stupid-silly.email@gmail.com'
    spoof = 'haha-email.com'

    print(bool(pattern.fullmatch(email)))
    print(bool(pattern.fullmatch(spoof)))


if __name__ == '__main__':
    main()

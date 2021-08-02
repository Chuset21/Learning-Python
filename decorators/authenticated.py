def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0].get('valid'):
            return fn(*args, **kwargs)

    return wrapper


@authenticated
def message_friends(user):
    name = user.get('name')
    print(f'Message has been sent to {name}.')


def main():
    user1 = {
        'name': 'Joe',
        'valid': True
    }
    message_friends(user1)


if __name__ == '__main__':
    main()

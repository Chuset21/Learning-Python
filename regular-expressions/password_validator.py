import re


# Password requirements:
# - Minimum 8 characters long
# - Contain at least one letter, one number and one symbol
class PasswordValidator:
    _PATTERN = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*\W)[A-Za-z\d\W]{8,}$")

    @staticmethod
    def validate_password(password):
        return PasswordValidator._PATTERN.fullmatch(str(password))


def main():
    valid_password = 'my9-dog@-yes'
    invalid_password = 'r*8'

    print(bool(PasswordValidator.validate_password(valid_password)))
    print(bool(PasswordValidator.validate_password(invalid_password)))


if __name__ == '__main__':
    main()

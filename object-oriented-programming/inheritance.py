class User:
    def __init__(self, email):
        self.email = email

    @staticmethod
    def attack():
        print('???')


class Wizard(User):
    def __init__(self, email, name, power):
        super().__init__(email)
        self.name = name
        self.power = power

    @staticmethod
    def attack():
        print('wizard attack')


class Archer(User):
    def __init__(self, email, name, num_arrows):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    @staticmethod
    def attack():
        print('archer attack')

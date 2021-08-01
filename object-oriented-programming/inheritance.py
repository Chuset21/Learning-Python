class User:
    def __init__(self, email, name):
        self.email = email
        self.name = name

    @staticmethod
    def attack():
        print('???')


class Wizard(User):
    def __init__(self, email, name, power):
        super().__init__(email, name)
        self.power = power

    def attack(self):
        print(f'wizard attack with power: {self.power}')


class Archer(User):
    def __init__(self, email, name, num_arrows):
        super().__init__(email, name)
        self.num_arrows = num_arrows

    def attack(self):
        print(f'{self.num_arrows} remaining')

    @staticmethod
    def run():
        print('run')


class HybridBorg(Wizard, Archer):
    def __init__(self, email, name, power, num_arrows):
        Archer.__init__(self, email, name, num_arrows)
        Wizard.__init__(self, email, name, power)

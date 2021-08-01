class PlayerCharacter:
    number_of_players = 0   # Doesn't change across instances

    def __init__(self, name='anonymous', age=0):
        if age > 16:
            PlayerCharacter.number_of_players += 1  # Example
            self._name = name
            self._age = age

    def __str__(self):
        return f'name = {self._name}, age = {self._age}'

    @staticmethod
    def run():
        print('run')

    @classmethod
    def adding_ages(cls, age1, age2):
        return cls(age=age1+age2)


def main():
    player1 = PlayerCharacter('Tom', 17)
    player2 = PlayerCharacter('Cindy', 44)

    print(PlayerCharacter.number_of_players)
    print(player1)
    help(PlayerCharacter)


if __name__ == '__main__':
    main()

"""
Доопрацюйте гру з заняття наступним чином:

1. Для обʼєкту классу Гравець при створенні питати їмʼя гравця, зберігати на обʼєкті.
2. Розширте гру новими ігровими фігурами. Скорегуйте поведінку всіх ігрових фігур під нові правила.
3. При оголошенні результатів гри повинно виводитись повідомлення "Гравець [імʼя гравця] переміг [імʼя гравця]
за допомогою [ігрова фігура]".
"""

from random import choice


class BasePlayer:
    name = 'Unknown'

    def get_figure(self, *args, **kwargs):
        return self._get_figure(*args, **kwargs)

    def _get_figure(self, *args, **kwargs):
        raise NotImplementedError


class HumanPlayer(BasePlayer):
    def __init__(self):
        self.name = input('Enter your name: ')

    def _get_figure(self, options: list):
        names = [obj.name for obj in options]
        while True:
            user_input = input(f'Enter one of the {names}: ')
            if user_input not in names:
                print('Wrong input')
                continue

            for obj in options:
                if obj.name == user_input:
                    return obj


class AIPlayer(BasePlayer):
    name = 'AI'

    def _get_figure(self, options: list):
        ai_choice = choice(options)
        print(f'HINT {ai_choice.name}')

        return ai_choice


class BaseGameFigure:
    def __eq__(self, other):
        if not isinstance(other, BaseGameFigure):
            raise TypeError
        return type(self) == type(other)


class Rock(BaseGameFigure):
    name = 'Rock'

    def __gt__(self, other):
        if not isinstance(other, BaseGameFigure):
            raise TypeError
        if isinstance(other, (Scissors, Lizard)):
            return True
        else:
            return False


class Scissors(BaseGameFigure):
    name = 'Scissors'

    def __gt__(self, other):
        if not isinstance(other, BaseGameFigure):
            raise TypeError
        if isinstance(other, (Paper, Lizard)):
            return True
        else:
            return False


class Paper(BaseGameFigure):
    name = 'Paper'

    def __gt__(self, other):
        if not isinstance(other, BaseGameFigure):
            raise TypeError
        if isinstance(other, (Rock, Spock)):
            return True
        else:
            return False


class Lizard(BaseGameFigure):
    name = 'Lizard'

    def __gt__(self, other):
        if not isinstance(other, BaseGameFigure):
            raise TypeError
        if isinstance(other, (Spock, Paper)):
            return True
        else:
            return False


class Spock(BaseGameFigure):
    name = 'Spock'

    def __gt__(self, other):
        if not isinstance(other, BaseGameFigure):
            raise TypeError
        if isinstance(other, (Scissors, Rock)):
            return True
        else:
            return False


class RSPGame:
    game_name = 'Rock Scissors Paper, Lizard, Spock'
    player1 = None
    player2 = None
    rules = [Scissors(), Paper(), Rock(), Lizard(), Spock()]

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def _play(self):
        f1 = self.player1.get_figure(self.rules)
        f2 = self.player2.get_figure(self.rules)

        if f1 == f2:
            print('Draw')
        elif f1 > f2:
            print(f'{self.player1.name} defeats {self.player2.name} with {f1.name}')
        else:
            print(f'{self.player2.name} defeats {self.player1.name} with {f2.name}')

    def play_3_times(self):
        print(f'{self.game_name} started for 3 time play')
        for _ in range(3):
            self._play()


ai_player = AIPlayer()
human_player = HumanPlayer()

game = RSPGame(ai_player, human_player)

game.play_3_times()

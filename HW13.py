"""
Доопрацюйте гру зі свого попереднього дз наступним чиноом:

1. Обʼєкт гри може отримати тільки обʼєкти класу Гравець.
2. Додайте до класу гри класметод, виклик якого виведе на екран інформацію про правила гри ("Гра [тут назва гри].
Гравцям потрібно обрати одну з фігур [тут перелік ігрових фігур з класу] і перемогти опонента")
"""

from random import choice
from abc import ABC, abstractmethod


class BaseAbstractPlayer(ABC):
    name = 'Unknown'

    @abstractmethod
    def get_figure(self, *args, **kwargs):
        pass


class HumanPlayer(BaseAbstractPlayer):
    def __init__(self):
        self.name = input('Enter your name: ')

    def get_figure(self, options: list):
        names = [obj.name for obj in options]
        while True:
            user_input = input(f'Enter one of the {names}: ')
            if user_input not in names:
                print('Wrong input')
                continue

            for obj in options:
                if obj.name == user_input:
                    return obj


class AIPlayer(BaseAbstractPlayer):
    name = 'AI'

    def get_figure(self, options: list):
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


class PlayerDescriptor:
    _name = None

    def __init__(self, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if not isinstance(value, BaseAbstractPlayer):
            raise TypeError
        instance.__dict__[self._name] = value


class RSPLSGame:
    game_message = ('Game "RSPLS" has started. Each player has to choose one of the figures '
                    '"Rock Scissors Paper, Lizard, Spock" and defeat an opponent.')
    _player1 = PlayerDescriptor('_player1')
    _player2 = PlayerDescriptor('_player2')
    rules = [Rock(), Scissors(), Paper(), Lizard(), Spock()]

    def __init__(self, player1, player2):
        self._player1 = player1
        self._player2 = player2

    @classmethod
    def get_from_cls(cls):
        print(cls.game_message)

    def play(self):
        self.get_from_cls()
        f1 = self._player1.get_figure(self.rules)
        f2 = self._player2.get_figure(self.rules)

        if f1 == f2:
            print('Draw')
        elif f1 > f2:
            print(f'{self._player1.name} defeats {self._player2.name} with {f1.name}')
        else:
            print(f'{self._player2.name} defeats {self._player1.name} with {f2.name}')


ai_player = AIPlayer()
human_player = HumanPlayer()

game = RSPLSGame(ai_player, human_player)

game.play()

"""
------------------------------------------------------------------------------------------------------------------------
GNU - General Public Licence v3
------------------------------------------------------------------------------------------------------------------------
Monopoly Simulator - By Piquipato
------------------------------------------------------------------------------------------------------------------------
This File contains the classes which defines the objects the program is going to be working with.

Classes:
1) Dice --> Simulates Dices on Monopoly.
    a) Regular --> Regular Dices. Random Integer from 1 to 6.
    b) Red --> Last Chance Dice.
2) Money --> With the Attributes of Cash and Currency.
3) Card --> This object simulates handheld cards in the board game.
    a) PropertyCards --> This object Simulates Property cards.
    b) Odds and Community Chest.
4) Property --> This are the Streets from Monopoly.
5) Board --> This is where the Game is Running.
    a) Space --> This is where Properties are located on the board.
------------------------------------------------------------------------------------------------------------------------
Link to Git Repository: https://github.com/Piquipato/Monopoly-in-Python.git
------------------------------------------------------------------------------------------------------------------------
"""


class Dice:

    """
        This Class Simulates Dices on Monopoly.
    """

    def __init__(self):

        import random
        self.value = random.randint(1, 6)   # Picks a random Integer between 1 and 6

    def __str__(self):

        return self.value

    def __add__(self, other):

        x = self.value + other.value
        return "{0} and {1} are equal to {2}".format(self.value, other.value, x)


class Money:

    """
        This Class Simulates Money in Monopoly.
    """

    def __init__(self, cash=1500.0, currency='€'):

        self.cash = cash
        self.currency = currency

    def __add__(self, other):

        if (isinstance(other, int)) or (isinstance(other, float)):
            return self.cash + other

        elif isinstance(other, Money):
            return self.cash + other.cash

        else:
            raise ValueError('Cash cannot be added up with the requested type: {0}'.format(type(other)))

    def __sub__(self, other):

        if (isinstance(other, int)) or (isinstance(other, float)):
            return self.cash - other

        elif isinstance(other, Money):
            return self.cash - other.cash

        else:
            raise ValueError('Cash cannot be added up with the requested type: {0}'.format(type(other)))
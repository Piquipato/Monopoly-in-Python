"""
------------------------------------------------------------------------------------------------------------------------
GNU - General Public Licence v3
------------------------------------------------------------------------------------------------------------------------
Monopoly Simulator - By Piquipato
------------------------------------------------------------------------------------------------------------------------
This File contains the classes which defines the objects the program is going to be working with.
Classes:
0) MonopolyGame --> Supreme Object. Contains all the Game in one.
1) Dice --> Simulates Dices on Monopoly.                                                        # DONE
    a) RegularDice --> Regular Dices. Random Integer from 1 to 6.
    b) LastChanceDice --> Last Chance Dice.
2) Money --> With the Attributes of Cash and Currency.                                          # DONE
3) Deck --> Simulates Card Decks on Monopoly
    a) Card --> This object simulates handheld cards in the board game.
        I) PropertyDeck --> Simulates the Properties Deck on Monopoly.
            i) PropertyCards --> This object Simulates Property cards.
        II) Chance/Chest Deck --> Simulates a Chance or a Community Chest Deck of Cards.
            ii) Chance and Community Chest.
4) Board --> Simulates a Monopoly Board
    a) Square --> Simulates a Square inside the Board.
5) Spaces --> Simulates all the Types of Spaces you can fall into -- Linked to Squares
    a) Property --> Simulates Properties on Monopoly.                                           # DONE
         I) Monopoly --> Simulates a Monopoly of Streets
             i) Street --> Simulates Streets on Monopoly.                                       # DONE
         II) Railroad --> Simulates Railroads.                                                  # DONE
         III) Utility --> Simulates Utilities.
    b) Tax --> Simulates a Tax Space.
    c) Chance/Chest --> Simulates a Chance/Community Chest Space.
    d) ParkingLot --> Simulates a ParkingLot Space.
    e) Prision
        i) Jail --> Simulates a Jail Space.
        ii) GoToJail --> Simulates a GoToJail Space.
6) Player --> Simulates a Player on Monopoly. It Rolls the dices to move around the Board. It can buy Properties.
    a) Human --> Human Player.
    b) AI --> Artificial Intelligence.
    c) Bank --> Auxiliary Artificial Intelligence which manages the Bank. Option to play with Limited/Unlimited Cash.
------------------------------------------------------------------------------------------------------------------------
Link to Git Repository: https://github.com/Piquipato/Monopoly-in-Python.git
------------------------------------------------------------------------------------------------------------------------
"""

# TODO: Create Classes listed above.
# TODO: Define their attributes and their methods.


class Monopoly:
    pass


class Statistics:
    pass


class Dice:

    """
        This Class Simulates Dices on Monopoly.
    """

    def __init__(self):

        import random
        self.value1 = random.randint(1, 6)   # Picks a random Integer between 1 and 6.
        self.value2 = random.randint(1, 6)
        self.x = self.value1 + self.value2

        print('{0} plus {1} = {2}'.format(self.value1, self.value2, self.x))
        player.move(self.x)


class ParkLotDice:

    """
       This Class is a pointer to the ParkingLot Space. For LastChanceDice Usage.
    """

    def __init__(self, player):

        self.space = Space()    # Not defined yet.

        player.moveTo(self.space)


class GoDice:

    """
        This Class is a pointer to the Go Space. For LastChanceDice Usage.
    """

    def __init__(self, player):

        self.space = Space()    # Not defined yet.

        player.moveTo(self.space)


class LastChanceDice:

    """
        This Class Simulates the Red Dice in Monopoly.
    """

    def __init__(self, player):

        import random
        self.value = random.randint(1, 6)

        if (self.value == 4) or (self.value == 5):
            x = GoDice(player)

        elif self.value == 6:
            x = ParkLotDice(player)

        else:
            player.move(self.value)


class Cash:

    """
        This Class Simulates Money in Monopoly.
    """

    def __init__(self, cash=1500.0, currency='€'):

        self.cash = cash
        self.currency = currency

    def __str__(self):
        return '{0}{1}'.format(self.cash, self.currency)

    def __neg__(self):
        return -self.cash

    def __pos__(self):
        return +self.cash

    def __invert__(self):
        return 1 / self.cash

    def __abs__(self):
        return abs(self.cash)

    def __add__(self, other):

        if (isinstance(other, int)) or (isinstance(other, float)):  # If other is an int object or a float object.
            return self.cash + other

        elif isinstance(other, Cash):   # If other is a Cash object.
            return self.cash + other.cash

        else:
            raise ValueError('Cash cannot be added up with the requested type: {0}'.format(type(other)))

    def __sub__(self, other):

        if (isinstance(other, int)) or (isinstance(other, float)):  # If other is an int object or a float object.
            return self.cash - other

        elif isinstance(other, Cash):   # If other is a Cash object.
            return self.cash - other.cash

        else:
            raise ValueError('Cash cannot be added up with the requested type: {0}'.format(type(other)))

    def __mul__(self, other):

        if (isinstance(other, int)) or (isinstance(other, float)):  # If other is an int object or a float object.
            return self.cash * other

        elif isinstance(other, Cash):   # If other is a Cash object.
            return self.cash * other.cash

        else:
            raise ValueError('Cash cannot be multiplied with the requested type: {0}'.format(type(other)))

    def __truediv__(self, other):

        if (isinstance(other, int)) or (isinstance(other, float)):  # If other is an int object or a float object.
            return self.cash / other

        elif isinstance(other, Cash):   # If other is a Cash object.
            return self.cash / other.cash

        else:
            raise ValueError('Cash cannot be divided with the requested type: {0}'.format(type(other)))

    def __floordiv__(self, other):

        if (isinstance(other, int)) or (isinstance(other, float)):  # If other is an int object or a float object.
            return self.cash // other

        elif isinstance(other, Cash):   # If other is a Cash object.
            return self.cash // other.cash

        else:
            raise ValueError('Cash cannot be divided with the requested type: {0}'.format(type(other)))

    def __mod__(self, other):

        if (isinstance(other, int)) or (isinstance(other, float)):  # If other is an int object or a float object.
            return self.cash % other

        elif isinstance(other, Cash):   # If other is a Cash object.
            return self.cash % other.cash

        else:
            raise ValueError('Cash cannot be divided with the requested type: {0}'.format(type(other)))

    def __divmod__(self, other):

        if (isinstance(other, int)) or (isinstance(other, float)):  # If other is an int object or a float object.
            return divmod(self.cash, other)

        elif isinstance(other, Cash):   # If other is a Cash object.
            return divmod(self.cash, other.cash)

        else:
            raise ValueError('Cash cannot be divided with the requested type: {0}'.format(type(other)))

    def __eq__(self, other):

        if (isinstance(other, int)) or (isinstance(other, float)):  # If other is an int object or a float object.
            if self.cash == other:
                return True
            else:
                return False
        elif isinstance(other, Cash):   # If other is a Cash object.
            if self.cash == other.cash:
                return True
            else:
                return False
        else:
            raise ValueError('Cash cannot be compared with the requested type: {0}'. format(type(other)))

    def __ne__(self, other):

        if (isinstance(other, int)) or (isinstance(other, float)):  # If other is an int object or a float object.
            if self.cash != other:
                return True
            else:
                return False
        elif isinstance(other, Cash):   # If other is a Cash object.
            if self.cash != other.cash:
                return True
            else:
                return False
        else:
            raise ValueError('Cash cannot be compared with the requested type: {0}'. format(type(other)))

    def __lt__(self, other):

        if (isinstance(other, int)) or (isinstance(other, float)):  # If other is an int object or a float object.
            if self.cash < other:
                return True
            else:
                return False
        elif isinstance(other, Cash):   # If other is a Cash object.
            if self.cash < other.cash:
                return True
            else:
                return False
        else:
            raise ValueError('Cash cannot be compared with the requested type: {0}'. format(type(other)))

    def __le__(self, other):

        if (isinstance(other, int)) or (isinstance(other, float)):  # If other is an int object or a float object.
            if self.cash <= other:
                return True
            else:
                return False
        elif isinstance(other, Cash):   # If other is a Cash object.
            if self.cash <= other.cash:
                return True
            else:
                return False
        else:
            raise ValueError('Cash cannot be compared with the requested type: {0}'. format(type(other)))

    def __gt__(self, other):

        if (isinstance(other, int)) or (isinstance(other, float)):  # If other is an int object or a float object.
            if self.cash > other:
                return True
            else:
                return False
        elif isinstance(other, Cash):   # If other is a Cash object.
            if self.cash > other.cash:
                return True
            else:
                return False
        else:
            raise ValueError('Cash cannot be compared with the requested type: {0}'. format(type(other)))

    def __ge__(self, other):

        if (isinstance(other, int)) or (isinstance(other, float)):  # If other is an int object or a float object.
            if self.cash >= other:
                return True
            else:
                return False
        elif isinstance(other, Cash):   # If other is a Cash object.
            if self.cash >= other.cash:
                return True
            else:
                return False
        else:
            raise ValueError('Cash cannot be compared with the requested type: {0}'. format(type(other)))


class Card:
    pass


class Deck:
    pass


class Hand(Deck):
    pass


class ChanceCard(Card):
    pass


class ChanceDeck(Deck):
    pass


class CommunityChestCard(Card):
    pass


class CommunityChestDeck(Deck):
    pass


class PropertyCard(Card):
    pass


class PropertyDeck(Deck):
    pass


class PropertyHand(Hand):
    pass


class PlotOfStreetsHand(Hand):
    pass


class Board:
    pass


class Square:
    pass


class Space:

    # TODO: Create Methods to work with Space Data.

    def __init__(self, Name, IdNum, Square):

        self.Name = Name
        self.IdNum = IdNum
        self.Square = Square

    def PlayerOnIt(self, Player):

        if Player.Position == self.Square:
            return True

        else:
            return False


class Property(Space):

    def __init__(self, Name, IdNum, Price, Rent, Mortgage=50, ReMortgage=110, StMortgage=False, CardNum=None):

        Space.__init__(Name, IdNum)
        self.Price = Price
        self.Rent = Rent
        self.Mortgage = Price * (Mortgage/100)
        self.ReMortgage = self.Mortgage * (ReMortgage/100)
        self.StMortgage = StMortgage



class Street(Property):
    pass


class PlotOfStreets(Street):
    pass


class Railroad(Property):
    pass


class Utility(Property):
    pass


class Tax(Space):
    pass


class Chance(Space):
    pass


class CommunityChest(Space):
    pass


class ParkingLot(Space):
    pass


class Jail:
    pass


class GoToJail:

    def __init__(self, player):

        if Property.PlayerOnIt(player=player):
            player.moveTo(Jail())


class Player:
    pass


class AI:
    pass


class AIPlayer(AI, Player):
    pass


class HumanPlayer(Player):
    pass


class Bank(AI):
    pass
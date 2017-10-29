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
    b) Chance and Community Chest.
4) Property --> This are the Streets from Monopoly.
5) Board --> This is where the Game is Running.
6) Space --> This is where Properties are located on the board.
7) Player --> Class which defines player information.
------------------------------------------------------------------------------------------------------------------------
Link to Git Repository: https://github.com/Piquipato/Monopoly-in-Python.git
------------------------------------------------------------------------------------------------------------------------
"""

# TO DO: Create Classes listed above.


class Player:

    # TO DO: Create Methods to work with Player Data.

    def __init__(self, idnum, name, space_in):

        # Initializes Player Object.

        self.id = idnum             # Integer. Identification Number.
        self.cash = Cash(1500)      # Cash Object. Amount of Cash on Hand.
        self.name = name            # String. Name of the Player.
        self.properties = []        # List of Properties.
        self.position = space_in    # Space Object. Position of the Player in the Board.
        self.out_of_jail_cards = 0  # Integer. Number of Out of Jail Cards the player is holding.
        self.jail_turns = 0         # Integer. Number of turns to Leave the Jail


class Space:

    # TO DO: Create Methods to work with Space Data.

    def __init__(self, position, assigned_property):

        # Initializes Space Object.

        self.position = position
        self.assigned_property = assigned_property

    def PlayerOnIt(self, player):

        # Checks if There is a player on the Space.

        if player.position == self.position:
            return True
        else:
            return False


class Board:

    # TO DO: Create Methods to work with Board Data.

    def __init__(self, space, properties):

        # Initializes Board Object.

        self.spaces = []
        for i in range(len(properties)):
            for x in properties:
                if x.id == i:
                    self.spaces.append(space.__init__(i, x))


class Dice:

    """
        This Class Simulates Dices on Monopoly.
    """

    def __init__(self):

        # Initializes Dice Object.

        import random
        self.value = random.randint(1, 6)   # Picks a random Integer between 1 and 6.

    def __str__(self):

        return self.value

    def __add__(self, other):

        x = self.value + other.value
        return "{0} and {1} are equal to {2}".format(self.value, other.value, x)


class Cash:

    # TO DO: Create Mathematical Methods within this class.

    """
        This Class Simulates Money in Monopoly.
    """

    def __init__(self, cash=1500.0, currency='€'):

        # Initializes Cash Object.

        self.cash = cash
        self.currency = currency

    def __add__(self, other):

        if (isinstance(other, int)) or (isinstance(other, float)):  # If other is an int object or a float object.
            return self.cash + other

        elif isinstance(other, Cash):   # If other is a Cash object.
            return self.cash + other.cash

        else:
            raise ValueError('Cash cannot be added up with the requested type: {0}'.format(type(other)))

    def __sub__(self, other):

        if (isinstance(other, int)) or (isinstance(other, float)):
            return self.cash - other

        elif isinstance(other, Cash):
            return self.cash - other.cash

        else:
            raise ValueError('Cash cannot be added up with the requested type: {0}'.format(type(other)))


class Property:

    # TO DO: Create Methods to work with Property data.

    def __init__(self, name, idnum, price, rent, mortgage, owner=None, mortgage_per=110, ismortgage=False):

        # Initializes Property Object.

        self.name = name                                    # String. Name of the Property.
        self.id = idnum                                     # Integer. Id of a Property to determine its Position.
        self.price = price                                  # Cash Object. Minimum Cash needed to Buy a Property.
        self.rent = rent                                    # Cash Object. Rent of the Property.
        self.owner = owner                                  # Player Object.
        self.mortgage = mortgage                            # Cash Object. Mortgage refund.
        self.rebuy_mort = mortgage * (mortgage_per / 100)   # Cash Object. Mortgage Rebuy.
        self.mortgage_status = ismortgage                   # Boolean. Mortgage Status.


class Street(Property):     # Inherits from Property.

    # TO DO: Create Methods to work with Street data.

    def __init__(self, name, space, color, price, price_building, rent, rent_building, owner=None, mortgage=False):

        # Initializes the Street Object

        Property.__init__(name, space, price, rent, owner, mortgage)

        self.color = color                      # Color Object. Color of Monopoly.
        self.price_building = price_building    # Tuple with Cash Objects. Building Prices.
        self.rent_monopoly = rent * 2           # Cash Object. Rent of the Property when Someone has Monopoly.
        self.rent_building = rent_building      # Tuple with Cash Objects. Rent of the Property with Buildings.
        self.number_buildings = 0               # Integer. Number of Buildings.


class Railroad(Property):

    # TO DO: Create Methods to work with Railroad Data.

    def __init__(self):

        # Initializes the Railroad Object

        self.rent_2 = self.rent * 2
        self.rent_3 = self.rent * 3
        self.rent_4 = self.rent * 4
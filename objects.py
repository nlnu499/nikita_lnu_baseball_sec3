"""
objects.py

Contains the business logic classes for the Baseball Team Manager.
Defines the Player and Lineup classes.
"""


class Player:
    """
    Represents a single baseball player.
    Stores player information and calculates batting average.
    """

    def __init__(self, first_name, last_name, position, at_bats, hits):
        """
        Initializes a Player object with basic statistics.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.at_bats = at_bats
        self.hits = hits

    @property
    def full_name(self):
        """
        Returns the player's full name.
        """
        return f"{self.first_name} {self.last_name}"

    @property
    def batting_average(self):
        """
        Calculates and returns the batting average.
        Returns 0.0 if at_bats is zero.
        """
        if self.at_bats == 0:
            return 0.0
        return round(self.hits / self.at_bats, 3)

    def update_position(self, new_position):
        """
        Updates the player's position.
        """
        self.position = new_position

    def update_stats(self, at_bats, hits):
        """
        Updates the player's statistics.
        """
        self.at_bats = at_bats
        self.hits = hits


class Lineup:
    """
    Manages a collection of Player objects.
   
    """

    def __init__(self):
        """
        Initializes an empty lineup.
        """
        self.__players = []

    def add_player(self, player):
        """
        Adds a Player object to the lineup.
        """
        self.__players.append(player)

    def remove_player(self, index):
        """
        Removes and returns a player by index.
        """
        return self.__players.pop(index)

    def move_player(self, old_index, new_index):
        """
        Moves a player from one position to another.
        """
        player = self.__players.pop(old_index)
        self.__players.insert(new_index, player)

    def get_player(self, index):
        """
        Returns a player by index.
        """
        return self.__players[index]

    def __len__(self):
        """
        Returns the number of players in the lineup.
        """
        return len(self.__players)

    def __iter__(self):
        """
        Allows iteration through the lineup using a for loop.
        """
        return iter(self.__players)
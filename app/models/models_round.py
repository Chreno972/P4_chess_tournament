"""The round's module

Returns:
    class: The round's class
"""


class Round:
    """the Round's class"""

    def __init__(self, name, start, finish, match_list):
        """The round's class initialization

        Args:
            name (str): The round's name
            start (datetime): The round's start date
            finish (datetime): The round's finish date
            match_list (list): The round's matches lists
        """
        self.name = name
        self.start = start
        self.finish = finish
        self.match_list = match_list

    def serialize_round(self):
        """Affords to serialize the player's informations

        Returns:
            Dict: contains the player's informations key, value pairs
        """
        serialized_round = {
            "name": self.name,
            "start_date": self.start,
            "finish_date": self.finish,
            "matches": self.match_list,
        }
        return serialized_round

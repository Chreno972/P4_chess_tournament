"""The players model

Returns:
    class: the player's class
"""


class Player:
    """The Player class"""

    def __init__(
        self,
        first_name,
        last_name,
        birthday,
        gender,
        rank,
        scores=float,
    ):
        """Player initialization

        Args:
            first_name (str): the player's first name
            last_name (str): the player's last name
            birthday (str): the players birthdate
            gender (str): the players gender "Male of Female"
            rank (int): the player's rank
            scores (float, optional): the player's score. Defaults to float.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.gender = gender
        self.rank = rank
        self.scores = scores

    def record_new_player(self):
        """Affords to insert all the player informations into a list

        Returns:
            list: contains each player's information
        """
        the_player = (
            self.first_name,
            self.last_name,
            self.birthday,
            self.gender,
            self.rank,
            self.scores,
        )
        return the_player

    def serialize_player(self):
        """Affords to seralise the player's informations

        Returns:
            Dict: contains key, value pairs of the player's informations
        """
        serialized_player = {
            "name": self.first_name + " " + self.last_name,
            "birthday": self.birthday,
            "gender": self.gender,
            "rank": self.rank,
            "scores": self.scores,
        }
        return serialized_player

class Match:
    def __init__(
        self,
        first_player,
        first_player_score,
        second_player,
        second_player_score,
    ):
        self.first_player = first_player
        self.first_player_score = first_player_score
        self.second_player = second_player
        self.second_player_score = second_player_score

    def serialize_match(self):
        the_match = {
            "first_player_name": self.first_player,
            "first_player_score": self.first_player_score,
            "second_player_name": self.second_player,
            "second_player_score": self.second_player_score,
        }
        return the_match

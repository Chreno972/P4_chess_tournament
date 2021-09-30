class Player:
    def __init__(
        self,
        first_name,
        last_name,
        birthday,
        gender,
        rank,
        scores=float,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.gender = gender
        self.rank = rank
        self.scores = scores

    def record_new_player(self):
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
        serialized_player = {
            "name": self.first_name + " " + self.last_name,
            "birthday": self.birthday,
            "gender": self.gender,
            "rank": self.rank,
            "scores": self.scores,
        }
        return serialized_player


if __name__ == "__main__":
    pass

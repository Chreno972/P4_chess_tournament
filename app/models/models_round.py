class Round:
    def __init__(self, name, start, finish, match_list):
        self.name = name
        self.start = start
        self.finish = finish
        self.match_list = match_list

    def serialize_round(self):
        serialized_round = {
            "name": self.name,
            "start_date": self.start,
            "finish_date": self.finish,
            "matches": self.match_list,
        }
        return serialized_round

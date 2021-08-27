class Tournaments:
    MAX_TURNS = 4

    def __init__(
        self,
        tournament_name,
        tournament_place,
        tournament_date,
        rounds,
        players,
        time_control,
    ):
        self.tournament_name = tournament_name
        self.tournament_place = tournament_place
        self.tournament_date = tournament_date
        self.rounds = rounds
        self.players = players
        self.time_control = time_control
        self.turns = self.MAX_TURNS

    def add_height_players(self):
        pass

    def create_tournament(self):
        pass

    def tournament_results(self):
        pass

    def make_players_pairs(self, players_list):
        pass

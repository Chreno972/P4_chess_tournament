class Tournaments:
    def __init__(
        self,
        tournament_name,
        tournament_place,
        tournament_date,
        time_control,
        rounds=None,
        players=None,
        turns=4,
    ):
        self.tournament_name = tournament_name
        self.tournament_place = tournament_place
        self.tournament_date = tournament_date
        self.rounds = rounds if rounds is not None else []
        self.players = players if players is not None else []
        self.time_control = time_control
        self.turns = turns

    def add_player(self, player):
        self.players.append(player)

    def tournament_results(self):
        pass

    def make_players_pairs(self, players_list):
        pass

class Match:
    MAX_PLAYERS = 2
    POSSIBLE_SCORE = [1, 0.5, 0]
    MATCH_COLORS = ["blacks", "whites"]

    def __init__(self, score, players_pair, player_results):
        self.player = players_pair
        self.score = score
        self.player_results = player_results

    def select_players_pair(self):
        pass

    def give_color(self):
        pass

    def match_messages(self):
        pass

    def generate_score(self, score):
        pass


class UniqueMatch(Match):
    def __init__(self, score, players=[]):
        pass


class MultipleMatchs(Match):
    def __init__(self, resultats_joueurs, players=[]):
        pass

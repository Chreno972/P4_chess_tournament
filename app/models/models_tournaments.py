from operator import itemgetter

# Installed libraries / modules imports
import numpy as np
import pandas as pd

# Created libraries / modules imports
from app.models.models_match import Match as mt

"""The tournament's model

Returns:
    class: The tournament's class
"""


class Tournaments:
    def __init__(
        self,
        admin,
        tournament_name=str,
        tournament_place=str,
        tournament_date=str,
        time_control=str,
        description=str,
        turns=4,
        rounds=None,
        players=None,
        winner=None,
    ):
        """The tournaments class initialization

        Args:
            admin (class): Une instance de la classe Admin
            tournament_name (str): the tournament's name
            tournament_place (str): the tournaments place
            tournament_date (str): the tournament's date
            time_control (str): the tournament's playing style
            description (str): the administrators give descriptions
            turns (int): the number of turns(rounds)
            rounds (list): A list of a tournament's rounds
            players (list): A list of a tournament's players
            winner (Dict): A dictionnary with the winner's informations
        """
        self.admin = admin
        self.turns = turns
        self.tournament_name = tournament_name
        self.tournament_place = tournament_place
        self.tournament_date = tournament_date
        self.time_control = time_control
        self.description = description
        self.rounds = rounds if rounds is not None else []
        self.players = players if players is not None else []
        self.winner = winner

    def record_tournament(self, tournament_table):
        tournament_table.insert(
            {
                "admin": self.admin,
                "turns": self.turns,
                "tournament_name": self.tournament_name,
                "tournament_place": self.tournament_place,
                "tournament_date": self.tournament_date,
                "time_control": self.time_control,
                "description": self.description,
                "rounds": self.rounds,
                "players": self.players,
                "winner": self.winner,
            }
        )

    def add_player(self, player):
        """Affords to add an instance of the Player's class
        into a list

        Args:
            player (list): contains each new instance of a Player
        """
        self.players.append(player)

    def generate_first_round(self):
        """Generates the first_round

        Returns:
            Dict:
            creates all the matches following the swiss rules
            inserts each match into a list
            creates a Round class instance,
            puts the match list into the instance of Round
            puts the instance of Rounds into the Tournament's rounds list
            then returns the updated player's scores
        """
        list_matchs = []
        match = {}
        for j, k in zip(range(0, 4), range(4, 8)):
            print(f"\nmatch {j}\n")
            match[j] = mt(
                self.players[j]["name"],
                float(input(f"score de {self.players[j]['name']}\n")),
                self.players[k]["name"],
                float(input(f"score de {self.players[k]['name']}\n")),
            ).serialize_match()

            self.players[j]["scores"] = match[j]["first_player_score"]
            self.players[k]["scores"] = match[j]["second_player_score"]

            list_matchs.append(match[j])
        return list_matchs

    def generate_other_round(self):
        """
        Generates all the other rounds according to
        the defined numbers of rounds by the administrator
        """
        sorted_list = sorted(self.players, key=itemgetter("scores"))
        list_matchs = []
        mat = {}
        for i, j, k in zip(
            range(0, 8, 2),
            range(1, 8, 2),
            range(1, 5),
        ):
            print(f"\nMatch {k}\n")
            mat[k] = mt(
                sorted_list[i]["name"],
                float(input(f"score de {sorted_list[i]['name']}\n")),
                sorted_list[j]["name"],
                float(input(f"score de {sorted_list[j]['name']}\n")),
            ).serialize_match()
            self.players[i]["scores"] += mat[k]["first_player_score"]
            self.players[j]["scores"] += mat[k]["second_player_score"]
            list_matchs.append(mat[k])
        return list_matchs

    def display_matches(self, the_list):
        matches_data = []
        matchs = []
        for i in range(1, len(the_list) + 1):
            matchs.append(f"Match {i}")
        for item in the_list:
            matches_data.append(
                [
                    item["first_player_name"],
                    item["first_player_score"],
                    "Scores",
                    item["second_player_score"],
                    item["second_player_name"],
                ]
            )
        data_numpy = np.array(matches_data, dtype=object)
        the_matches = pd.DataFrame(
            data_numpy,
            index=matchs,
            columns=[
                "JOUEUR 1",
                "SCORE 1",
                "RÉSULTATS",
                "SCORE 2",
                "JOUEUR 2",
            ],
        )
        print(the_matches)

    def display_scores(self):
        get_players_scores = []
        participants = []
        for k in range(1, 9):
            participants.append(f"Participant {k}")
        for i in range(0, 8):
            get_players_scores.append(
                [
                    self.players[i]["name"],
                    self.players[i]["scores"],
                ]
            )
        converting_in_numpy_array = np.array(get_players_scores, dtype=object)
        dps = pd.DataFrame(
            converting_in_numpy_array,
            index=participants,
            columns=["NOM", "SCORES"],
        )
        print(dps.sort_values(by=["SCORES"], ascending=False))


if __name__ == "__main__":
    pass

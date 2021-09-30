from app.models.models_round import Round as rd
from app.models.models_admin import Admin as adm


import numpy as np
import pandas as pd


from datetime import datetime as dt
from operator import itemgetter


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

    def __repr__(self):
        re = (
            self.tournament_name,
            self.tournament_place,
            self.tournament_date,
        )
        return re

    def add_player(self, player):
        self.players.append(player)

    def generate_first_round(self):
        print(f"\nROUND 1 DU TOURNOI {self.tournament_name}\n")
        # générer la liste des matchs
        list_matchs = []
        match1 = {
            "first_player_name": self.players[0]["name"],
            "first_player_score": float(
                input(f"Quel est le score de {self.players[0]['name']} ?\n")
            ),
            "second_player_name": self.players[4]["name"],
            "second_player_score": float(
                input(f"Quel est le score de {self.players[4]['name']} ?\n")
            ),
        }
        self.players[0]["scores"] = match1["first_player_score"]
        self.players[4]["scores"] = match1["second_player_score"]
        match2 = {
            "first_player_name": self.players[1]["name"],
            "first_player_score": float(
                input(f"Quel est le score de {self.players[1]['name']} ?\n")
            ),
            "second_player_name": self.players[5]["name"],
            "second_player_score": float(
                input(f"Quel est le score de {self.players[5]['name']} ?\n")
            ),
        }
        self.players[1]["scores"] = match2["first_player_score"]
        self.players[5]["scores"] = match2["second_player_score"]
        match3 = {
            "first_player_name": self.players[2]["name"],
            "first_player_score": float(
                input(f"Quel est le score de {self.players[2]['name']} ?\n")
            ),
            "second_player_name": self.players[6]["name"],
            "second_player_score": float(
                input(f"Quel est le score de {self.players[6]['name']} ?\n")  # vues
            ),
        }
        self.players[2]["scores"] = match3["first_player_score"]  # controller
        self.players[6]["scores"] = match3["second_player_score"]
        match4 = {
            "first_player_name": self.players[3]["name"],
            "first_player_score": float(
                input(f"Quel est le score de {self.players[3]['name']} ?\n")
            ),
            "second_player_name": self.players[7]["name"],
            "second_player_score": float(
                input(f"Quel est le score de {self.players[7]['name']} ?\n")
            ),
        }
        self.players[3]["scores"] = match4["first_player_score"]
        self.players[7]["scores"] = match4["second_player_score"]

        list_matchs = [match1, match2, match3, match4]
        print("\nRésultats du Round 1\n")
        self.display_matches(list_matchs)
        # créer l'objet round
        round = rd(
            "Round 1",
            "dt",
            "13/09/2021 à 20h00",
            list_matchs,
        )
        ser_round = {
            "name": round.name,
            "start_date": round.start,
            "finish_date": round.finish,
            "matches": round.match_list,
        }
        # # ajouter le round à la liste des rounds du tournoi (self)
        self.rounds.append(ser_round)
        print()
        self.display_scores()
        print(f"\nFin du {ser_round['name']}\n")
        return self.players

    def generate_other_round(self):
        if int(self.turns) > 1:
            iter = 0
            next_round = 2
            while iter < int(self.turns) - 1:
                try:
                    print(
                        "\nROUND {} DU TOURNOI {}\n".format(
                            next_round, self.tournament_name
                        )
                    )
                    round_started = dt.now().strftime("%d-%m-%Y %H:%M:%S")
                    sorted_list = sorted(self.players, key=itemgetter("scores"))
                    list_matchs = []
                    match1 = {
                        "first_player_name": sorted_list[0]["name"],
                        "first_player_score": float(
                            input(f"Quel est le score de {sorted_list[0]['name']} ?\n")
                        ),
                        "second_player_name": sorted_list[1]["name"],
                        "second_player_score": float(
                            input(f"Quel est le score de {sorted_list[1]['name']} ?\n")
                        ),
                    }
                    self.players[0]["scores"] += match1["first_player_score"]
                    self.players[1]["scores"] += match1["second_player_score"]
                    match2 = {
                        "first_player_name": sorted_list[2]["name"],
                        "first_player_score": float(
                            input(f"Quel est le score de {sorted_list[2]['name']} ?\n")
                        ),
                        "second_player_name": sorted_list[3]["name"],
                        "second_player_score": float(
                            input(f"Quel est le score de {sorted_list[3]['name']} ?\n")
                        ),
                    }
                    self.players[2]["scores"] += match2["first_player_score"]
                    self.players[3]["scores"] += match2["second_player_score"]
                    match3 = {
                        "first_player_name": sorted_list[4]["name"],
                        "first_player_score": float(
                            input(f"Quel est le score de {sorted_list[4]['name']} ?\n")
                        ),
                        "second_player_name": sorted_list[5]["name"],
                        "second_player_score": float(
                            input(f"Quel est le score de {sorted_list[5]['name']} ?\n")
                        ),
                    }
                    self.players[4]["scores"] += match3["first_player_score"]
                    self.players[5]["scores"] += match3["second_player_score"]
                    match4 = {
                        "first_player_name": sorted_list[6]["name"],
                        "first_player_score": float(
                            input(f"Quel est le score de {sorted_list[6]['name']} ?\n")
                        ),
                        "second_player_name": sorted_list[7]["name"],
                        "second_player_score": float(
                            input(f"Quel est le score de {sorted_list[7]['name']} ?\n")
                        ),
                    }
                    self.players[6]["scores"] += match4["first_player_score"]
                    self.players[7]["scores"] += match4["second_player_score"]

                    list_matchs = [match1, match2, match3, match4]
                    print("\nRésultats du Round\n")
                    self.display_matches(list_matchs)
                    self.display_scores()
                    round = rd(
                        "Round {}".format(next_round),
                        round_started,
                        "13/09/2021 à 20h00",
                        list_matchs,
                    )
                    ser_round = {
                        "name": round.name,
                        "start_date": round.start,
                        "finish_date": round.finish,
                        "matches": round.match_list,
                    }
                    self.rounds.append(ser_round)
                    print("\nFin du round {}\n".format(next_round))
                    ser_round["finish_date"] = dt.now().strftime("%d-%m-%Y %H%M:%S")
                    next_round += 1
                    iter += 1
                except Exception:
                    print("ALERTE -- ALERTE -- ALERTE -- ALERTE !!!!!!")
                    break
            the_winner = max(self.players, key=lambda x: x["scores"])
            win_place = {
                "name": the_winner["name"],
                "score": the_winner["scores"],
            }
            self.winner.append(win_place)
            print(
                "Tournoi '{}' terminé le {}. \n{} le remporte avec un score total de {} points.\n".format(
                    self.tournament_name,
                    dt.now().strftime("%d-%m-%Y à %H heures %M"),
                    the_winner["name"].upper(),
                    the_winner["scores"],
                )
            )

    def display_matches(self, the_list):
        matches_data = []
        matchs = []
        for i in range(1, 5):
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

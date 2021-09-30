# Python libraries / modules imports
import os
from time import sleep as sl
import csv

# Installed libraries / modules imports
import numpy as np
import pandas as pd

# Created libraries / modules imports
from app.data.db import TOURNAMENTS_TABLE as tournaments_table
from app.views.ViewsReportsMenu import RViews as r_views


class Reports:
    def __init__(self):
        self.views = r_views(self)

    def main_reports_menu(self):
        choice = self.views.reports_menu_choices()
        if choice == "1":
            self.display_tournament_players()
        elif choice == "2":
            self.display_tournaments()
            input("\nAppuyez sur entrée pour continuer!")
            self.main_reports_menu()
        elif choice == "3":
            self.display_all_participants()
        elif choice == "4":
            self.display_tournament_matches()
        elif choice == "5":
            os.system("exit()")
        else:
            print("Tapez un numéro de choix répertorié!")
            sl(2)
            self.main_reports_menu()

    def display_tournament_players(self):
        """Afficher les joueurs d'un tournoi"""

        tournament_choice = self.views.get_tournament_id()
        data = []
        for item in tournaments_table:
            if str(item.doc_id) == tournament_choice:
                for i in range(8):
                    data.append(
                        [
                            item["players"][i]["name"],
                            item["players"][i]["birthday"],
                            item["players"][i]["gender"],
                            item["players"][i]["rank"],
                            item["players"][i]["scores"],
                        ]
                    )
        data_numpy2 = np.array(data, dtype=object)
        the_list = pd.DataFrame(
            data_numpy2,
            columns=[
                "NAME",
                "BIRTHDAY",
                "GENDER",
                "RANK",
                "SCORES",
            ],
        )
        choice = self.views.display_order_choices()
        if choice == "1":
            print(the_list.sort_values(by=["NAME"], ascending=True))
            input("\nAppuyez sur entrée pour continuer!")
            self.main_reports_menu()
        elif choice == "2":
            print(the_list.sort_values(by=["RANK"], ascending=True))
            input("\nAppuyez sur entrée pour continuer!")
            self.main_reports_menu()
        elif choice == "3":
            print(the_list.sort_values(by=["SCORES"], ascending=False))
            input("Appuyez sur entrée pour continuer!")
            self.main_reports_menu()
        elif choice == "4":
            print(the_list)
            input("Appuyez sur entrée pour continuer!")
            self.main_reports_menu()
        else:
            print("Veuillez entre un choix correct")
            sl(3)
            self.main_reports_menu()

    def display_all_participants(self):
        participants = []
        administrators = []
        indexes = []
        for item in tournaments_table:
            administrators.append(
                [
                    item["admin"]["name"],
                    item["tournament_name"],
                    "Admin",
                    0,
                ]
            )
            for i in range(8):
                participants.append(
                    [
                        item["players"][i]["name"],
                        item["tournament_name"],
                        "Joueur",
                        int(item["players"][i]["rank"]),
                    ]
                )
        participants.extend(administrators)
        for i in range(0, len(participants)):
            i = ""
            indexes.append(i)
        pt_numpy = np.array(participants)
        all_participants = pd.DataFrame(
            pt_numpy,
            index=indexes,
            columns=[
                "PARTICIPANTS",
                "ALL TOURNAMENTS",
                "QUALITY",
                "RANK",
            ],
        )
        choice = self.views.display_order_choices()
        if choice == "1":
            print(all_participants.sort_values(by=["PARTICIPANTS"], ascending=True))
            input("\nAppuyez sur entrée pour continuer!")
            self.main_reports_menu()
        elif choice == "2":
            print(all_participants.sort_values(by=["RANK"], ascending=True))
            input("\nAppuyez sur entrée pour continuer!")
            self.main_reports_menu()
        elif choice == "3":
            print(all_participants)
            input("\nAppuyez sur entrée pour continuer!")
            self.main_reports_menu()
        else:
            print("Veuillez entrer un choix correct")
            sl(3)
            self.main_reports_menu()

    def display_tournament_matches(self):
        tournament_choice = self.views.get_tournament_id()
        data = []
        for item in tournaments_table:
            if str(item.doc_id) == tournament_choice:
                for el in item["rounds"]:
                    for i, j in zip(range(0, 4), range(1, 5)):
                        data.append(
                            [
                                el["name"],
                                f"match {j}",
                                el["matches"][i]["first_player_name"],
                                el["matches"][i]["first_player_score"],
                                el["matches"][i]["second_player_name"],
                                el["matches"][i]["second_player_score"],
                            ]
                        )
        data_numpy = np.array(data, dtype=object)
        match_list = pd.DataFrame(
            data_numpy,
            columns=[
                "ROUNDS",
                "MATCHS",
                "PLAYER 1",
                "SCORE 1",
                "PLAYER 2",
                "SCORE 2",
            ],
        )
        print(match_list)

    def display_tournaments(self):
        data = []
        indexes = []
        for i in range(len(tournaments_table)):
            i = "TOURNOI"
            indexes.append(i)
        for item in tournaments_table:
            data.append(
                [
                    item.doc_id,
                    item["admin"]["name"],
                    item["tournament_name"],
                    item["tournament_place"],
                    item["tournament_date"],
                    item["time_control"],
                    item["description"],
                    item["turns"],
                    item["winner"][0]["name"],
                    item["winner"][0]["score"],
                ]
            )
        data_numpy = np.array(data, dtype=object)
        players_list = pd.DataFrame(
            data_numpy,
            index=indexes,
            columns=[
                "ID",
                "ADMINISTRATEUR",
                "NOM DU TOURNOI",
                "LIEU DU TOURNOI",
                "DATE DE LANCEMENT",
                "STYLE DE JEU",
                "DESCRIPTION",
                "NB TOURS",
                "LE GAGNANT",
                "SON SCORE",
            ],
        )
        print()
        print(players_list.sort_values(by=["NOM DU TOURNOI"]))
        print()


if __name__ == "__main__":
    Reports().main_reports_menu()

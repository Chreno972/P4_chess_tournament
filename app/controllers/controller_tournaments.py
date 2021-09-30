# Python libraries / modules imports
import os
from time import sleep as sl
from datetime import datetime as dt

# Installed libraries / modules imports
import numpy as np
import pandas as pd

# Created libraries / modules imports
from app.data.db import TOURNAMENTS_TABLE as tournaments_table
from app.models.models_player import Player
from app.models.models_admin import Admin
from app.models.models_tournaments import Tournaments
from app.views.view_main_menu import MainViewMenu as mvm
from app.views.ViewsTournamentsMenu import Views as vtm
from app.controllers.controller_reports import Reports as rps


class Controller:
    """[summary]"""

    def __init__(self):
        self.views = vtm(self)
        self.main_view = mvm(self)

    def main_menu(self):
        mm = self.main_view.main_menu()
        if mm == "1":
            self.tournaments_menu_choices()
        elif mm == "2":
            rps().main_reports_menu()
        elif mm == "3":
            os.system("exit()")

    def tournaments_menu_choices(self):
        choice = self.views.tournament_menu_choices()
        if choice == "1":
            self.create_new_tournament()
        elif choice == "2":
            self.main_menu()
        elif choice == "3":
            self.quit_application()
        else:
            print("Tapez un numéro de choix répertorié!")
            sl(2)
            self.tournaments_menu_choices()

    def create_player(self):
        result = self.views.add_new_player()
        player = Player(
            result[0],
            result[1],
            result[2],
            result[3],
            int(result[4]),
            0,
        )
        return player.serialize_player()

    def create_admin(self):
        result = self.views.add_new_admin()
        admin = Admin(
            result[0],
            result[1],
        )
        return admin.serialize_admin()

    def create_new_tournament(self):
        result = self.views.create_tournament()
        les_joueurs = []
        for i, j in zip(range(8), range(1, 9)):
            print("\nAJOUT DU JOUEUR N° {}\n".format(j))
            i = self.create_player()
            les_joueurs.append(i)
        tournament = Tournaments(
            self.create_admin(),
            result[0],
            result[1],
            self.generate_date(),
            result[2],
            result[3],
            result[4],
            result[5],
            les_joueurs,
            [],
        )
        self.tournament = tournament
        # tournament.record_tournament(tournaments_table)
        print("Parfait, votre Tournoi est crée et vos joueurs ajoutés.\n")
        sl(2)
        self.tournament.generate_first_round()
        self.tournament.generate_other_round()
        self.tournament.record_tournament(tournaments_table)
        input("Appuyez sur entrée pour continuer!")
        sl(2)
        self.tournaments_menu_choices()

    def generate_date(self):
        now = dt.now().strftime("%d-%m-%Y %H:%M:%S")
        return now

    def quit_application(self):
        print("Merci de votre visite, Aurevoir")
        sl(2)
        os.system("exit()")

    def back_to_main_menu(self):
        self.tournaments_menu_choices()


if __name__ == "__main__":
    Controller().main_menu()

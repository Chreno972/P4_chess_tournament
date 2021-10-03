"""The controller_tournaments module

Returns:
    class: The controller_tournaments class
"""
# Python libraries / modules imports
import os
from time import sleep as sl
from datetime import datetime as dt

# Created libraries / modules imports
from app.data.db import TOURNAMENTS_TABLE as tournaments_table
from app.models.models_player import Player
from app.models.models_admin import Admin
from app.models.models_tournaments import Tournaments
from app.views.view_main_menu import MainViewMenu as mvm
from app.views.ViewsTournamentsMenu import Views as vtm
from app.controllers.controller_reports import Reports as rps


class Controller:
    """The controller_tournaments class"""

    def __init__(self):
        """initialize views"""
        self.views = vtm(self)
        self.main_view = mvm(self)

    def main_menu(self):
        """The main view controls"""
        main_menu_result = self.main_view.main_menu()
        if main_menu_result == "1":
            self.tournaments_menu_choices()
        elif main_menu_result == "2":
            rps().main_reports_menu()
        elif main_menu_result == "3":
            os.system("exit()")

    def tournaments_menu_choices(self):
        """Tournament choices controls"""
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
        """Method to create players

        Returns:
            class instance: an instance of the Player class
            allied with its serialize_player method
        """
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
        """Method to create admin

        Returns:
            class instance: an instance of the Admin class
            allied with its serialize_admin method
        """
        result = self.views.add_new_admin()
        admin = Admin(
            result[0],
            result[1],
        )
        return admin.serialize_admin()

    def create_new_tournament(self):
        """Method to create a tournament"""
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
            dt.now().strftime("%d-%m-%Y %H:%M:%S"),
            result[2],
            result[3],
            result[4],
            result[5],
            les_joueurs,
            [],
        )
        tournament
        # tournament.record_tournament(tournaments_table)
        print("Parfait, votre Tournoi est crée et vos joueurs ajoutés.\n")
        sl(2)
        tournament.generate_first_round()
        tournament.generate_other_round()
        tournament.record_tournament(tournaments_table)
        input("Appuyez sur entrée pour continuer!")
        sl(2)
        self.tournaments_menu_choices()

    def quit_application(self):
        """Method to quit application"""
        print("Merci de votre visite, Aurevoir")
        sl(2)
        os.system("exit()")

    def back_to_main_menu(self):
        """Method to get back to the main menu"""
        self.tournaments_menu_choices()


if __name__ == "__main__":
    """launches the game"""
    Controller().main_menu()

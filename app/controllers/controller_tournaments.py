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
from app.models.models_round import Round as rd
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
        self.launch_first_round(tournament)
        self.launch_other_rounds(tournament)
        tournament.record_tournament(tournaments_table)
        input("Appuyez sur entrée pour continuer!")
        sl(2)
        self.tournaments_menu_choices()

    def launch_first_round(self, tournoi):
        print(f"\nROUND 1 DU TOURNOI {tournoi.tournament_name}\n")
        generation = tournoi.generate_first_round()
        print("\nRésultats du Round 1\n")
        tournoi.display_matches(generation)
        round_started = dt.now().strftime("%d-%m-%Y %H:%M:%S")
        round = rd(
            "Round 1",
            round_started,
            "13/09/2021 à 20h00",
            generation[0],
        )
        ser = {
            "name": round.name,
            "start_date": round.start,
            "finish_date": round.finish,
            "matches": round.match_list,
        }
        tournoi.rounds.append(ser)
        print()
        print(f"Fin du {ser['name']}")
        return tournoi.players

    def launch_other_rounds(self, tournoi):
        if int(tournoi.turns) > 1:
            iter = 0
            next_round = 2
            nb_match = 1
            round_started = dt.now().strftime("%d-%m-%Y %H:%M:%S")
            while iter < int(tournoi.turns) - 1:
                generation = tournoi.generate_other_round()
                print(
                    "\nROUND {} DU TOURNOI {}\n".format(
                        next_round, tournoi.tournament_name
                    )
                )

                print("\nRésultats du Round {}\n".format(next_round))
                tournoi.display_matches(generation)
                round = rd(
                    "Round {}".format(next_round),
                    round_started,
                    "13/09/2021 à 20h00",
                    generation[0],
                )
                ser = {
                    "name": round.name,
                    "start_date": round.start,
                    "finish_date": round.finish,
                    "matches": round.match_list,
                }
                tournoi.rounds.append(ser)
                print("\nFin du round {}\n".format(next_round))
                sl(2)
                ser["finish_date"] = dt.now().strftime("%d-%m-%Y %H:%M:%S")
                next_round += 1
                iter += 1
                nb_match += 1
            the_winner = max(tournoi.players, key=lambda x: x["scores"])
            win_place = {
                "name": the_winner["name"],
                "score": the_winner["scores"],
            }

            tournoi.display_scores()
            print()
            tournoi.winner.append(win_place)
            print(
                "'{}' terminé le {}. \nGagnant: {} score {} points.\n".format(
                    tournoi.tournament_name,
                    dt.now().strftime("%d-%m-%Y à %H heures %M"),
                    the_winner["name"].upper(),
                    the_winner["scores"],
                )
            )

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

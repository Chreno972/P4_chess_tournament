class RViews(object):
    def __init__(self, r_controller):
        self.r_controller = r_controller

    def reports_menu_choices(self):

        print("MENU DES REPORTS\n")
        print("Choix 1 - Liste des joueurs d'un tournoi")
        print("Choix 2 - Liste de tous les tournois")
        print("Choix 3 - Liste de tous les acteurs")
        print("Choix 4 - Liste des matchs d'un tournoi")
        print("Choix 5 - Quitter l'application\n")
        reports_menu_choice = input("Faites votre choix :\n")
        return reports_menu_choice

    def get_tournament_id(self):
        self.r_controller.display_tournaments()
        tournament_id = input("\nQuel est l'id du tournoi ? ")
        return tournament_id

    def display_order_choices(self):
        print("Choix 1 - Vue par ordre alphabétique ?")
        print("Choix 2 - Vue par ordre de classement ?")
        print("Choix 3 - Vue par ordre d'enregistrement ?")
        choice = input("\nFaites votre choix :\n")
        return choice

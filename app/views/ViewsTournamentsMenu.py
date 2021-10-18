class Views(object):
    """
    All the views for the tournament
    """

    def __init__(self, controller):
        self.controller = controller

    def tournament_menu_choices(self):
        """Make your choice for the tournament

        Returns:
            str: the string number that represents the choice
        """
        print("MENU DES TOURNOIS\n")
        # self.controller.display_players()
        print("Choix 1 - Créer un tournoi")
        print("Choix 2 - Retourner au menu principal")
        print("Choix 3 - Quitter\n")
        tournaments_menu_choice = input("Faites votre choix : ")
        return tournaments_menu_choice

    def add_new_player(self):
        """Make your choices to create a player

        Returns:
            list: a list of variables
        """

        prenom = input("prenom du participant : ")
        nom = input("nom du participant : ")
        birthday = input("sa date naissance 00/00/0000 : ")
        genre = input("son genre M ou F : ")
        classement = input("son classement : ")
        score = None
        return [prenom, nom, birthday, genre, classement, score]

    def add_new_admin(self):
        """Name your new admin

        Returns:
            list: a list of variables
        """
        admin_prename = input("quel est votre prénom d'administrateur ?\n")
        admin_name = input("Quel est votre nom d'administrateur ?\n")
        return [admin_prename, admin_name]

    def create_tournament(self):
        """Enter your choices to create a tournament

        Returns:
            list: a list of variables
        """
        print("CRÉER UN TOURNOI\n")
        tournament_name = input("Quel sera son nom ? ")
        tournament_place = input("Son lieu ? ")
        time_control = input("bullet, blitz ou coup rapide ? ")
        tournament_description = input("Description du tournoi : ")
        turns = input("Le nombre de tours / Défaut 4 ? ")
        rounds = None
        players = None
        return [
            tournament_name,
            tournament_place,
            time_control,
            tournament_description,
            turns,
            rounds,
            players,
        ]

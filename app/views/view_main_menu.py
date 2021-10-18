class MainViewMenu(object):
    """
    The main menu choices
    """

    def __init__(self, controller):
        self.controller = controller

    def main_menu(self):
        """Make your first choice

        Returns:
            str: your choice
        """
        print("MENU PRINCIPAL")
        print("Choix 1 - Menu des Tournois")
        print("Choix 2 - Menu des Reports")
        print("Choix 3 - Quitter\n")
        main_choice = input("Faites votre choix : ")
        return main_choice

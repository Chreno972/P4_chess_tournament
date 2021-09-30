class MainViewMenu(object):
    """
    class docstrings
    """

    def __init__(self, controller):
        self.controller = controller

    def main_menu(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        print("MENU PRINCIPAL")
        print("Choix 1 - Menu des Tournois")
        print("Choix 2 - Menu des Reports")
        print("Choix 3 - Quitter\n")
        main_choice = input("Faites votre choix : ")
        return main_choice

from app.views.PlayerView import PlayerView
from app.controllers.controller import MainController


def run_tournament():
    MainController.main_menu()


if __name__ == "__main__":
    run_tournament()
    print(PlayerView.get_player_from_input())

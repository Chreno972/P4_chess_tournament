"""Importe la classe controller du tournoi
"""
from app.controllers.controller_tournaments import Controller


def run_tournament():
    """Lance le menu principal"""
    Controller().main_menu()


if __name__ == "__main__":
    run_tournament()

from app.models.models_player import Player


class PlayerView:
    @classmethod
    def get_player_from_input(cls):
        return Player(
            first_name=input("prénom"),
            last_name=input("nom : "),
            bday=input("bday"),
            sex=input("sex"),
            rank=input("rank :"),
        )


if __name__ == "__main__":
    print(PlayerView.get_player_from_input())

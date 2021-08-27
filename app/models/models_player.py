class Player:
    def __init__(self, first_name, last_name, bday, sex, rank, score=0):
        self.first_name = first_name
        self.last_name = last_name
        self.bday = bday
        self.sex = sex
        self.rank = rank
        self.score = score

    def __repr__(self):
        name = f"{self.first_name} {self.last_name}"
        re = f"""
        {name}
        Né le: {self.bday} 
        de sexe {self.sex}
        de rang {self.rank}"""

        return re

    @classmethod
    def from_input(cls):
        return Player(
            first_name=input("prénom"),
            last_name=input("nom : "),
            bday=input("bday"),
            sex=input("sex"),
            rank=input("rank :"),
        )

    def win(self):
        self.score += 1

    def draw(self):
        self.score += 0.5

    def lose(self):
        self.score += 0


if __name__ == "__main__":
    player = Player("Réno", "Christophe", "12/09/1988", "Masculin", 521457, 2)
    player2 = Player.from_input()
    print(player)
    print(player2)
    # print(player.__repr__())

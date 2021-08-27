class Player:
    def __init__(self, first_name, last_name, bday, sex, rank, score):
        self.first_name = first_name
        self.last_name = last_name
        self.bday = bday
        self.sex = sex
        self.rank = rank
        self.rank = score

    def play_game(self):
        pass

    def __repr__(self):
        name = f"{self.first_name} {self.last_name}"
        re = f"""
        {name}
        Né le: {self.bday} 
        de sexe {self.sex}
        de rang {self.rank}"""

        return re


player = Player("Réno", "Christophe", "12/09/1988", "Masculin", 521457, 2)

# print(player.__repr__())

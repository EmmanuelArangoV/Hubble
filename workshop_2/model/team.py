from workshop_2.model.player import Player
class Team:
    def __init__(self, name):
        self.name = name
        self.members: list[Player] = []
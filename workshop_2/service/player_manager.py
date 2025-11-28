from workshop_2.model.player import *
from workshop_2.service.password_crypt import *
from workshop_2.service.utils import *
from workshop_2.service.teams_manager import TeamManager

class PlayerManager:
    def __init__(self):
        self.players: list[Player] = []
        self.persistence = True

    def add_player(self, player: Player):
        self.players.append(player)
        print(ctext(f"Player {player.name} added successfully!", "success"))

    def id_exists(self, id: str) -> bool:
        for player in self.players:
            if player.id == id:
                return True
        return False

    def login(self, id: str, password: str) -> bool:
        for player in self.players:
            if player.id == id:
                return verify_password(password, player.password)
        return False

    def delete_player(self, id: str, teamManager: TeamManager) -> bool:
        for player in self.players:
            if player.id == id:
                teamManager.delete_member(player.team, id)
                self.players.remove(player)
                return True
        return False

    def get_player(self, id: str) -> Player | None:
        for player in self.players:
            if player.id == id:
                return player
        return None

    def list_players(self):
        if not self.players:
            print(ctext("There's no players registered", "warning"))
        for player in self.players:
            print(ctext(f"ID: {player.id} | Name: {player.name} | Role: {player.role} | Team: {player.team} ", "info"))

    def get_players_no_team(self):
        flag = False
        print(ctext("=== AVAILABLE PLAYERS ===", 'info'))
        for player in self.players:
            if player.team == "N/A":
                print(ctext(f"ID: {player.id} | Name: {player.name} | Role: {player.role}", 'info'))
                flag = True
        if not flag:
            print(ctext("No players available without a team.", 'warning'))

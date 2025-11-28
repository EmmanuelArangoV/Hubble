from workshop_2.model.player import *
from workshop_2.service.password_crypt import *
from workshop_2.service.utils import *
from workshop_2.service.teams_manager import TeamManager

class PlayerManager:
    def __init__(self, players):
        self.players: list[Player] = players
        self.file_path = 'persistence/users.csv'

    def add_player(self, player: Player):
        self.players.append(player)
        self.save_players()
        print(ctext(f"Player {player.name} added successfully!", "success"))

    def id_exists(self, id: str) -> bool:
        for player in self.players:
            if player.id == id:
                return True
        return False

    def login(self, id: str, password: str) -> Player | None:
        for player in self.players:
            if player.id == id and verify_password(password, player.password):
                return player
        return None

    def delete_player(self, id: str, teamManager: TeamManager) -> bool:
        player_to_delete = self.get_player(id)
        if player_to_delete:
            if player_to_delete.team != "N/A":
                teamManager.delete_member(player_to_delete.team, id)
            self.players.remove(player_to_delete)
            self.save_players()
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
            return
        for player in self.players:
            print(ctext(f"ID: {player.id} | Name: {player.name} | Role: {player.role} | Team: {player.team} ", "info"))

    def get_players_no_team(self):
        available_players = [p for p in self.players if p.team == "N/A"]
        if not available_players:
            print(ctext("No players available without a team.", 'warning'))
            return

        print(ctext("=== AVAILABLE PLAYERS ===", 'info'))
        for player in available_players:
            print(ctext(f"ID: {player.id} | Name: {player.name} | Role: {player.role}", 'info'))

    def save_players(self):
        from workshop_2.persistence.files_manager import save_users
        save_users(self.players)

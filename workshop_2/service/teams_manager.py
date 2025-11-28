from workshop_2.service.utils import *
from workshop_2.model.team import Team
from workshop_2.model.player import Player

class TeamManager:
    def __init__(self, teams):
        self.teams: list[Team] = teams

    def add_team(self, team: Team):
        self.teams.append(team)
        self.save_teams()

    def list_teams(self):
        if not self.teams:
            print(ctext("No teams registered yet.", "warning"))
            return
        for team in self.teams:
            print(ctext(f"Team Name: {team.name} | Members: {len(team.members)}", "prompt"))

    def delete_team(self, team_name: str, player_manager) -> bool:
        team_to_delete = self.get_team(team_name)
        if team_to_delete:
            for member in team_to_delete.members:
                player = player_manager.get_player(member.id)
                if player:
                    player.team = "N/A"
            player_manager.save_players()
            self.teams.remove(team_to_delete)
            self.save_teams()
            return True
        return False

    def delete_member(self, team_name: str, member_id: str) -> bool:
        team = self.get_team(team_name)
        if team:
            member_to_remove = None
            for member in team.members:
                if member.id == member_id:
                    member_to_remove = member
                    break
            if member_to_remove:
                team.members.remove(member_to_remove)
                self.save_teams()
                return True
        return False

    def assign_player_to_team(self, player: Player, team_name: str) -> bool:
        team = self.get_team(team_name)
        if team:
            team.members.append(player)
            player.team = team_name
            self.save_teams()
            return True
        return False

    def name_available(self, name: str) -> bool:
        return not any(team.name.lower() == name.lower() for team in self.teams)

    def role_available_in_team(self, team_name: str, role: str) -> bool:
        team = self.get_team(team_name)
        if team:
            return not any(member.role.lower() == role.lower() for member in team.members)
        return True

    def get_team(self, team_name: str) -> Team | None:
        for team in self.teams:
            if team.name.lower() == team_name.lower():
                return team
        return None

    def save_teams(self):
        from workshop_2.persistence.files_manager import save_teams
        save_teams(self.teams)

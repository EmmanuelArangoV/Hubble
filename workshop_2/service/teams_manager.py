from workshop_2.service.utils import *
from workshop_2.model.team import Team
from workshop_2.service.player_manager import PlayerManager

class TeamManager:
    def __init__(self):
        self.teams: list[Team] = []

    def add_team(self, team: Team):
        self.teams.append(team)

    def list_teams(self):
        for team in self.teams:
            print(ctext(f"Team Name: {team.name} | Number of members: {len(self.teams)}", "prompt"))

    def delete_team(self, team_name: str) -> bool:
        for team in self.teams:
            if team.name == team_name:
                for member in team.members:
                    member.team = "N/A"
                self.teams.remove(team)
                return True
        return False

    def delete_member(self, team_name: str, member_id: str) -> bool:
        for team in self.teams:
            if team.name == team_name:
                for member in team.members:
                    if member.id == member_id:
                        team.members.remove(member)
                        member.team = "N/A"
                        return True
        return False

    def assign_player_to_team(self, player_manager: PlayerManager, player_id: str, team_name: str) -> bool:
        player = player_manager.get_player(player_id)
        if not player:
            return False
        for team in self.teams:
            if team.name == team_name:
                team.members.append(player)
                player.team = team_name
                return True
        return False

    def name_available(self, name: str) -> bool:
        for team in self.teams:
            if team.name.lower() == name.lower():
                return False
        return True

    def role_available_in_team(self, team_name: str, role: str) -> bool:
        for team in self.teams:
            if team.name == team_name:
                for member in team.members:
                    if member.role.lower() == role.lower():
                        return False
        return True

    def get_team(self, team_name: str) -> Team | None:
        for team in self.teams:
            if team.name == team_name:
                return team
        return None
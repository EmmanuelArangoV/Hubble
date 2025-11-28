from workshop_2.service.player_manager import PlayerManager
from workshop_2.service.teams_manager import TeamManager
from workshop_2.service.utils import *


def ask_team_name(team: TeamManager) -> str:
    while True:
        raw = input(ctext("Product name: ", 'prompt')).capitalize()
        try:
            name = valid_string(raw)
            if not team.name_available(name):
                print(ctext("Name already exists. Try another.", 'warning'))
                continue
            return name
        except ValueError as e:
            print(ctext(str(e), 'error'))

def ask_team_member(player_manager: PlayerManager, team_m: TeamManager):
    team_name = input(ctext("Enter the team name to add a member to: ", 'prompt')).strip()
    try:
        team_name = valid_string(team_name)
        team = team_m.get_team(team_name)
        if not team:
            raise ValueError("Team does not exist.")
    except ValueError as e:
        print(ctext(str(e), 'error'))
        return

    while True:
        print(ctext("==== ADD TEAM MEMBER ====", 'info'))
        player_manager.get_players_no_team()

        player_id = input(ctext("Enter the ID of the player to add: ", 'prompt')).strip()
        player = player_manager.get_player(player_id)
        if not player:
            print(ctext("No player found with that ID. Try again.", 'error'))
            continue
        if player.team != "N/A":
            print(ctext("Player is already assigned to a team. Choose another player.", 'warning'))
            continue





def verify_role_availability(team: TeamManager, team_name: str, role: str) -> bool:
    if not team.role_available_in_team(team_name, role):
        print(ctext(f"A player with the role '{role}' already exists in the team '{team_name}'.", 'warning'))
        return False
    return True

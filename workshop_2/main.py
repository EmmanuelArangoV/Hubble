from controller import main_menu
from service.player_manager import PlayerManager
from service.teams_manager import TeamManager
from persistence.files_manager import load_users, load_teams

def main():
    players = load_users()
    teams = load_teams()

    player_manager = PlayerManager(players)
    team_manager = TeamManager(teams)

    main_menu(player_manager, team_manager)

if __name__ == "__main__":
    main()


from service.player_manager import PlayerManager
from service.teams_manager import TeamManager
from service.utils import *
from model.player import Player
from model.team import Team
from service.password_crypt import hash_password

# --- Main Orchestrator ---

def main_menu(player_manager: PlayerManager, team_manager: TeamManager):
    """Handles user login and directs to the appropriate menu."""
    print(ctext("--- WELCOME TO THE SPORTS MANAGEMENT SYSTEM ---", "header"))
    user = login_user(player_manager)
    if not user:
        print(ctext("Exiting...", "info"))
        return

    if user.role.lower() == 'admin':
        admin_menu(player_manager, team_manager)
    else:
        player_menu(user)

def login_user(player_manager: PlayerManager) -> Player | None:
    """Handles the user login process."""
    attempts = 3
    while attempts > 0:
        user_id = input(ctext("Enter your ID: ", "prompt"))
        password = input(ctext("Enter your password: ", "prompt"))
        user = player_manager.login(user_id, password)
        if user:
            print(ctext("Login successful!", "success"))
            return user

        attempts -= 1
        print(ctext(f"Invalid ID or password. You have {attempts} attempts left.", "error"))

    print(ctext("Too many failed login attempts.", "error"))
    return None

# --- Player Menu ---

def player_menu(player: Player):
    """Displays the player's data."""
    print(ctext(f"\n--- Welcome, {player.name} ---", "header"))
    print(ctext(f"ID: {player.id}", "info"))
    print(ctext(f"Role: {player.role}", "info"))
    print(ctext(f"Team: {player.team}", "info"))
    input(ctext("\nPress Enter to exit.", "prompt"))

# --- Admin Menus ---

def admin_menu(player_manager: PlayerManager, team_manager: TeamManager):
    while True:
        print(ctext("\n--- ADMIN MENU ---", "header"))
        print("1. Player Management")
        print("2. Team Management")
        print("3. Exit")
        choice = input(ctext("Enter your choice: ", "prompt"))

        match choice:
            case '1':
                player_management_menu(player_manager, team_manager)
            case '2':
                team_management_menu(player_manager, team_manager)
            case '3':
                break
            case _:
                print(ctext("Invalid choice. Please try again.", "warning"))

# --- Player Management ---

def player_management_menu(player_manager: PlayerManager, team_manager: TeamManager):
    while True:
        print(ctext("\n--- PLAYER MANAGEMENT ---", "header"))
        print("1. Add Player")
        print("2. List Players")
        print("3. Delete Player")
        print("4. Back to Admin Menu")
        choice = input(ctext("Enter your choice: ", "prompt"))

        match choice:
            case '1':
                add_player_flow(player_manager)
            case '2':
                player_manager.list_players()
            case '3':
                delete_player_flow(player_manager, team_manager)
            case '4':
                break
            case _:
                print(ctext("Invalid choice.", "warning"))

def add_player_flow(player_manager: PlayerManager):
    print(ctext("--- Add New Player ---", "info"))
    try:
        id = ask_player_id(player_manager)
        name = valid_string(input(ctext("Player name: ", "prompt")))
        role = "Player"
        password = hash_password(input(ctext("Password: ", "prompt")))

        player = Player(id, name, role, password, "N/A")
        player_manager.add_player(player)
    except ValueError as e:
        print(ctext(str(e), 'error'))

def delete_player_flow(player_manager: PlayerManager, team_manager: TeamManager):
    print(ctext("--- Delete Player ---", "info"))
    player_id = input(ctext("Enter the ID of the player to delete: ", "prompt"))
    if not player_manager.id_exists(player_id):
        print(ctext("Player ID not found.", "error"))
        return

    if player_manager.delete_player(player_id, team_manager):
        print(ctext("Player deleted successfully.", "success"))
    else:
        print(ctext("Failed to delete player.", "error"))


def ask_player_id(player_manager: PlayerManager) -> str:
    while True:
        id = input(ctext("Player ID: ", "prompt"))
        if player_manager.id_exists(id):
            print(ctext("This ID is already taken. Try another.", "warning"))
        else:
            return id

# --- Team Management ---

def team_management_menu(player_manager: PlayerManager, team_manager: TeamManager):
    while True:
        print(ctext("\n--- TEAM MANAGEMENT ---", "header"))
        print("1. Add Team")
        print("2. List Teams")
        print("3. Add Player to Team")
        print("4. Delete Team")
        print("5. Back to Admin Menu")
        choice = input(ctext("Enter your choice: ", "prompt"))

        match choice:
            case '1':
                add_team_flow(team_manager)
            case '2':
                team_manager.list_teams()
            case '3':
                add_player_to_team_flow(player_manager, team_manager)
            case '4':
                delete_team_flow(team_manager, player_manager)
            case '5':
                break
            case _:
                print(ctext("Invalid choice.", "warning"))

def add_team_flow(team_manager: TeamManager):
    print(ctext("--- Add New Team ---", "info"))
    try:
        name = ask_team_name(team_manager)
        team = Team(name)
        team_manager.add_team(team)
        print(ctext(f"Team '{name}' created successfully!", "success"))
    except ValueError as e:
        print(ctext(str(e), 'error'))

def delete_team_flow(team_manager: TeamManager, player_manager: PlayerManager):
    """Guides the admin through deleting a team."""
    print(ctext("--- Delete Team ---", "info"))
    team_name = input(ctext("Enter the name of the team to delete: ", "prompt"))
    if not team_manager.get_team(team_name):
        print(ctext("Team not found.", "error"))
        return

    if team_manager.delete_team(team_name, player_manager):
        print(ctext(f"Team '{team_name}' deleted successfully.", "success"))
    else:
        print(ctext("Failed to delete team.", "error"))


def add_player_to_team_flow(player_manager: PlayerManager, team_manager: TeamManager):
    print(ctext("--- Add Player to Team ---", "info"))
    team_name = input(ctext("Enter team name: ", "prompt"))
    team = team_manager.get_team(team_name)
    if not team:
        print(ctext("Team not found.", "error"))
        return

    player_manager.get_players_no_team()
    player_id = input(ctext("Enter player ID to add: ", "prompt"))
    player = player_manager.get_player(player_id)

    if not player or player.team != "N/A":
        print(ctext("Invalid player ID or player already in a team.", "error"))
        return

    if team_manager.assign_player_to_team(player, team.name):
        player_manager.save_players()
        print(ctext("Player added to team successfully.", "success"))
    else:
        print(ctext("Failed to add player to team.", "error"))


def ask_team_name(team_manager: TeamManager) -> str:
    while True:
        name = valid_string(input(ctext("Team name: ", "prompt")).capitalize())
        if not team_manager.name_available(name):
            print(ctext("This name is already taken. Try another.", "warning"))
        else:
            return name

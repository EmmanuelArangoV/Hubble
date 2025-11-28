import csv
import os
from workshop_2.model.player import Player
from workshop_2.model.team import Team

USERS_FILE = 'persistence/users.csv'
TEAMS_FILE = 'persistence/teams.json'

def load_users():
    if not os.path.exists(USERS_FILE):
        return []

    players = []
    with open(USERS_FILE, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            players.append(Player(**row))
    return players

def save_users(players: list[Player]):
    with open(USERS_FILE, mode='w', newline='') as file:
        fieldnames = ['id', 'name', 'role', 'password', 'team']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for player in players:
            writer.writerow(player.__dict__)

def load_teams():
    import json
    if not os.path.exists(TEAMS_FILE):
        return []

    teams = []
    with open(TEAMS_FILE, 'r') as file:
        teams_data = json.load(file)
        for team_data in teams_data:
            team = Team(team_data['name'])
            team.members = team_data.get('members', [])
            teams.append(team)
    return teams


def save_teams(teams: list[Team]):
    import json
    with open(TEAMS_FILE, 'w') as file:
        teams_data = []
        for team in teams:
            teams_data.append({
                'name': team.name,
                'members': [p.id for p in team.members] # Save player IDs
            })
        json.dump(teams_data, file, indent=4)

import bcrypt
import csv

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

users = [
    {'id': 'admin', 'name': 'Admin User', 'role': 'Admin', 'password': hash_password('password'), 'team': 'N/A'},
    {'id': 'player1', 'name': 'Player One', 'role': 'Player', 'password': hash_password('password'), 'team': 'N/A'},
    {'id': 'player2', 'name': 'Player Two', 'role': 'Player', 'password': hash_password('password'), 'team': 'N/A'},
    {'id': 'player3', 'name': 'Player Three', 'role': 'Player', 'password': hash_password('password'), 'team': 'N/A'},
    {'id': 'player4', 'name': 'Player Four', 'role': 'Player', 'password': hash_password('password'), 'team': 'N/A'},
    {'id': 'player5', 'name': 'Player Five', 'role': 'Player', 'password': hash_password('password'), 'team': 'N/A'}
]

file_path = '/workshop_2/persistence/users.csv'
fieldnames = ['id', 'name', 'role', 'password', 'team']

with open(file_path, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(users)

print(f"File '{file_path}' created successfully with new passwords.")


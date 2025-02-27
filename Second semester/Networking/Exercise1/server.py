import socket
from questions import question_data
import json

def load_user():
    """Load user data from a JSON file."""
    try:
        with open('users.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_user(u):
    """Save user data to a JSON file."""
    with open('users.json', 'w') as f:
        json.dump(u, f)

def create_password():
    """Create a password with basic validation."""
    while True:
        password = input("Enter a password (at least 6 characters): ")
        if len(password) >= 6:  # Example rule: minimum length of 6 characters
            return password
        else:
            print("Password too short. Please enter a password of at least 6 characters.")

def register_user(username, password):
    """Register a new user."""
    users = load_user()
    if username in users:
        return "User already exists."
    else:
        users[username] = {
            'password': password,  # Store plain-text password (not recommended for real applications)
            'score': 0,
            'rank': 0
        }
        save_user(users)
        return "User registered successfully."

def login_user(username, password):
    """Log in a user by checking their credentials."""
    users = load_user()
    if username in users and users[username]['password'] == password:
        return True
    else:
        return False

# Server setup
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 100))
s.listen()

client_socket, address = s.accept()
print("A client from address ", address, " connected.")

# Ask for username and password for registration or login
client_socket.sendall("Enter 'register' or 'login' to continue: ".encode('utf-8'))
action = client_socket.recv(1024).decode('utf-8')

client_socket.sendall("Enter username: ".encode('utf-8'))
user_name = client_socket.recv(1024).decode('utf-8')

client_socket.sendall("Enter password: ".encode('utf-8'))
password = client_socket.recv(1024).decode('utf-8')

if action.lower() == 'register':
    message = register_user(user_name, password)
    client_socket.sendall(message.encode('utf-8'))
elif action.lower() == 'login':
    if login_user(user_name, password):
        client_socket.sendall("Login successful. Starting the game...".encode('utf-8'))
    else:
        client_socket.sendall("Invalid username or password.".encode('utf-8'))
        client_socket.close()
        exit()

# Proceed with the game if login is successful
questions_length = len(question_data)
client_socket.sendall(f'Hei {user_name}, the number of questions available is: {questions_length}. Provide how many you want to answer.'.encode('utf-8'))

score = 0
question = 0
number_of_questions = 0

# Receive client's response with the number of questions
message_client = client_socket.recv(1024)
decode_message = message_client.decode('utf-8').split()
for element in decode_message:
    if element.isdigit():
        number_of_questions = int(element)
        break

# Start the quiz
while question < number_of_questions:
    q = question_data[question]['text']
    a = question_data[question]['answer'].lower()

    client_socket.sendall(f'Question {question + 1}: {q} (true/false)'.encode('utf-8'))
    answer = client_socket.recv(1024).decode('utf-8')
    if answer == a:
        score += 1

    question += 1

# Update and save the user's score
users = load_user()
if user_name in users:
    # Update the user's score if it's higher than the previous score
    if users[user_name]['score'] < score:
        users[user_name]['score'] = score

save_user(users)

# Sort the users by their scores in descending order
sorted_users = sorted(users.keys(), key=lambda x: users[x]['score'], reverse=True)

# Establish ranks based on their score
rank = 1
for user in sorted_users:
    users[user]['rank'] = rank
    rank += 1

# Save the updated user data
save_user(users)

# Tell the user their rank in comparison to others
client_socket.sendall(f'Your final score: {score}'.encode('utf-8'))

for user in sorted_users:
    if user != user_name:
        client_socket.sendall(f"User {user} is ranked {users[user]['rank']} with score {users[user]['score']}.".encode('utf-8'))

client_socket.close()
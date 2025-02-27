import socket

# Create a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 100))

# Select the type of action (login or register)
action = input("Enter 'register' or 'login' to continue: ")
s.sendall(action.encode('utf-8'))

# Send the username and password
username = input("Enter username: ")
s.sendall(username.encode('utf-8'))
password = input("Enter password: ")
s.sendall(password.encode('utf-8'))

# Receive the confirmation message
message = s.recv(1024).decode('utf-8')
print(message)

if "successful" in message.lower() or "login successful" in message.lower():
    # Receive the number of questions
    message = s.recv(1024).decode('utf-8')
    print(message)

    # Send the number of questions you want to answer
    number_of_questions = input()
    s.sendall(number_of_questions.encode('utf-8'))

    question = 0

    # Start quiz
    while question < int(number_of_questions):
        message = s.recv(1024).decode('utf-8')
        print(message)

        if 'Your final score' in message:  # Check for final
            break

        answer = input().lower()
        s.sendall(answer.encode('utf-8'))
        question += 1

    # Receive the final score
    score = s.recv(1024).decode('utf-8')
    print(score)

# Close the connection
s.close()
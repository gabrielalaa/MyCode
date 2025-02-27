import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect(('localhost', 9999))
action = input("Would you like to play Hangman game? (yes/no)").lower()

# lives = 6
if action == 'yes':
    # Request for a hangman game
    s.sendall(action.encode('utf-8'))

    word_length = s.recv(1024).decode('utf-8')
    print(word_length)

    # # Send the first character to guess
    # character = input("Your character: ").lower()
    # s.sendall(character.encode('utf-8'))

    while True:
        # Send characters to the server
        character = input("Your character: ").lower()
        s.sendall(character.encode('utf-8'))

        # Get the response from the server (it may be a loose, a win or the continuity of the game
        response = s.recv(1024).decode('utf-8')

        if 'lose' in response:
            print(response)
            break

        if 'win' in response:
            print(response)
            break

        print(response)

s.close()
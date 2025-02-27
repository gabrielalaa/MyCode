import socket
import random

def choose_a_random_word():
    with open('words.txt', 'r') as f:
        selected_word = random.choice(f.readlines()).strip()
        return selected_word

def check_character(char, output_list, word):
    # Only update output_list with correct guesses
    if char in word:
        for position in range(len(word)):
            if word[position] == char:
                output_list[position] = char
    return output_list


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 9999))
s.listen()

client_socket, address = s.accept()
print('A client from the ', address, ' just connected')

action = client_socket.recv(1024).decode('utf-8')

# If the client wants to play, start the game
lives = 6
word = choose_a_random_word()
word_length = len(word)
output_list = ['_'] * word_length
char_list = []

if action == 'yes':
    # Send the information about the length of the word
    client_socket.sendall(f"Hei client! The word you have to choose has length: {len(word)}".encode('utf-8'))

    while lives > 0:
        # Receive characters and check them
        character = client_socket.recv(1024).decode('utf-8')

        # Check if the character was previously introduced
        if character in char_list:
            client_socket.sendall(f"You already said this character {character}".encode('utf-8'))
            continue
        else:
            char_list.append(character)

        # Update output_list based on the guessed character
        output_list = check_character(character, output_list, word)

        # In case the character was not in the word, -1 lives
        if character not in word:
            lives -= 1

        # Check if the client lose
        if lives == 0:
            client_socket.sendall(f"You lose... The word was: {word}".encode('utf-8'))
            break

        # Check if the client wins
        if ''.join(output_list) == word:
            client_socket.sendall(f"You win! The word was: {word}".encode('utf-8'))
            break

        # Send the evolution of the game
        client_socket.sendall(f"Your guess: {''.join(output_list)}. Your lives: {lives}. Enter a new character: ".encode('utf-8'))

client_socket.close()
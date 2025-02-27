import socket
import threading
from TicTacToe import Tictactoe

connected_clients = 0
lock = threading.Lock()
client_sockets = []
client_names = []

def handle_client(addr, c_socket):
    global connected_clients, client_names, client_sockets

    # Receive client name
    client_name = c_socket.recv(1024).decode('utf-8')

    with lock:
        if connected_clients >= 2:
            c_socket.send(b'Sorry client! You are not able to connect. Two players are in game now.')
            c_socket.close()
            return
        else:
            connected_clients += 1
            client_sockets.append(c_socket)
            client_names.append(client_name)
            print(f"Client {client_name} ({addr}) connected. Total clients: {connected_clients}")
            c_socket.send(f"Welcome {client_name}".encode('utf-8'))

    # Start game if two clients are connected
    if connected_clients == 2:
        start_game()

    # Keep the connection open for messages or disconnects
    try:
        while True:
            pass  # Keep the connection open
    except Exception as e:
        print(f"Error with client {addr}: {e}")
    finally:
        with lock:
            connected_clients -= 1
            client_sockets.remove(c_socket)
            client_names.remove(client_name)
        print(f"Client {client_name} ({addr}) disconnected. Total clients: {connected_clients}")
        c_socket.close()

def start_game():
    game = Tictactoe(client_names[0], client_names[1])
    client_sockets[0].send(f"init@gameid {client_names[0]} vs {client_names[1]}".encode('utf-8'))
    client_sockets[1].send(f"init@gameid {client_names[0]} vs {client_names[1]}".encode('utf-8'))

    current_turn = 0  # 0 for player1, 1 for player2

    while not game.gameWon()[0]:
        current_player_socket = client_sockets[current_turn]
        other_player_socket = client_sockets[1 - current_turn]
        current_player_socket.send(f"Your turn. Current Board:\n{game.getBoardTxt()}".encode('utf-8'))
        other_player_socket.send(f"Waiting for opponent's move... Current Board:\n{game.getBoardTxt()}".encode('utf-8'))

        move = int(current_player_socket.recv(1024).decode('utf-8'))

        if game.board[move - 1] != 'X' and game.board[move - 1] != 'O':
            game.makeMove(move)
            end, winner = game.gameWon()
            if end:
                client_sockets[0].send(f"GameEnd! Player {winner} wins!\nFinal Board:\n{game.getBoardTxt()}".encode('utf-8'))
                client_sockets[1].send(f"GameEnd! Player {winner} wins!\nFinal Board:\n{game.getBoardTxt()}".encode('utf-8'))
                break
            current_turn = 1 - current_turn  # Switch turn
        else:
            current_player_socket.send("Invalid move, try again.".encode('utf-8'))

# Create a TCP server socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 8080))
s.listen()

while True:
    # Accept incoming client connections
    client_socket, address = s.accept()

    # Start a new thread to handle the client
    t1 = threading.Thread(target=handle_client, args=(address, client_socket))
    t1.start()
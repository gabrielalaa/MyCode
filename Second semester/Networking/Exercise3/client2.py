import socket

# Client connects to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8080))

# Client sends its name
name = input('Enter your name: ')
s.sendall(name.encode('utf-8'))

while True:
    message = s.recv(1024).decode('utf-8')
    print(message)
    if "Your turn" in message:
        move = input("Enter your move (1-9): ")
        s.send(move.encode('utf-8'))
    elif "GameEnd" in message:
        break

s.close()
import socket

# Connecting to a local server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 5050))

# msg = b"Hi Server" # can also use .encode('utf-8')
#
# s.send(msg)
# message_from_server = s.recv(1024)

msg = ''
while msg != 'bye':
    msg = input("What do you want to send to the server? ")

    s.send(msg.encode('utf-8'))

    server_answer = s.recv(1024)
    server_answer = server_answer.decode('utf-8')
    print(f"Got this message from server: {server_answer}")

s.close()
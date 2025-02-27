import socket
from datetime import datetime

# Create a TCP server socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Bind it to a port number
s.bind(("localhost", 5050))
# Listen for incoming requests
s.listen()

# Blocking Operation
# (wait until a client connects)
client_socket, address = s.accept()
print("A client from ", address, " connected.")

# # Receive 1024 bytes from client
# message_from_client = client_socket.recv(1024)
# print('Got the message', message_from_client)
# # Reply to the client
# client_socket.sendall((b"Hello in return!"))

while True:
    # Receive 1024 bytes from client - when you print message_client directly without decoding, you may see unexpected results/extra characters!
    message_client = client_socket.recv(1024)
    decoded_message = message_client.decode("utf-8")
    print("Got this message: ", decoded_message)

    if decoded_message == "bye":
        break

    # Reply to the client
    client_socket.sendall('Hei client!'.encode("utf-8"))

    # formatRequested = message_client.decode("utf-8")
    # if not message_client:
    #     break

# Reply to the client
# client_socket.sendall(datetime.now().strftime(formatRequested).encode("utf-8"))
# Close connection to the client
# Sends an empty string!
# client_socket.close()
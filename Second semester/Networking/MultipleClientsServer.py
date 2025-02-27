import socket
import threading

def handle_client(address, client_socket):
    print("A client from ", address, " connected.")

    while True:
        # Receive message from client
        message_client = client_socket.recv(1024)
        decoded_message = message_client.decode("utf-8")
        print("Got this message: ", decoded_message)

        # Check for termination message
        if decoded_message.lower() == "bye":
            print("Client from ", address, " disconnected.")
            break

        # Send response to client
        client_socket.sendall('Hei client!'.encode("utf-8"))

    # Close client socket after communication ends
    client_socket.close()

# Create a TCP server socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 5050))
s.listen()

print("Server listening on port 5050...")

while True:
    # Accept incoming client connections
    client_socket, address = s.accept()

    # Start a new thread to handle the client
    t1 = threading.Thread(target=handle_client, args=(address, client_socket))
    t1.start()
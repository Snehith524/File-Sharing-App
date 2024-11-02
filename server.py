import socket
import os

HOST = '0.0.0.0'  
PORT = 5001       
BUFFER_SIZE = 4096  
SEPARATOR = "<SEPARATOR>"

def send_file(filename):
    if not os.path.isfile(filename):
        print(f"Error: '{filename}' not found.")
        return

    # Set up the server socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Server is waiting for a connection on {HOST}:{PORT}...")

        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print(f"Connected to client at {client_address}")

        # Send filename and file size to client
        filesize = os.path.getsize(filename)
        client_socket.send(f"{filename}{SEPARATOR}{filesize}".encode())

        # Send the file in chunks
        with open(filename, "rb") as file:
            while data := file.read(BUFFER_SIZE):
                client_socket.sendall(data)
        print(f"File '{filename}' sent successfully.")

        client_socket.close()

if __name__ == "__main__":
    filename = "info.txt"  # Specify the file to send
    send_file(filename)

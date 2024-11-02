import socket

HOST = '127.0.0.1'
PORT = 5001
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

def receive_file():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print(f"Connected to server at {HOST}:{PORT}")

        received = client_socket.recv(BUFFER_SIZE).decode()
        filename, filesize = received.split(SEPARATOR)
        filesize = int(filesize)

        with open(filename, "wb") as file:
            print(f"Receiving '{filename}'...")
            bytes_received = 0
            
            while bytes_received < filesize:
                data = client_socket.recv(BUFFER_SIZE)
                if not data:
                    break
                file.write(data)
                bytes_received += len(data)

        print(f"File '{filename}' received successfully.")

if __name__ == "__main__":
    receive_file()

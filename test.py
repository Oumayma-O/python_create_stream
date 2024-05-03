import socket

def main():
    port = 9999  # The same port as used by the server

    # Create a socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('172.27.145.119', port))

    try:
        while True:
            # Receive data from the server
            data = client_socket.recv(1024)
            if data:
                print('Received:', data.decode('utf-8'))
            else:
                break
    finally:
        # Close the socket when done
        client_socket.close()

if __name__ == "__main__":
    main()
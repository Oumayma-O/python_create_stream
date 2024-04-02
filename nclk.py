import socket

def main():
    port = 9999  # Port number to listen on

    # Start a socket server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(1)
    print(f"Listening on port {port}")
    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address}")

        while True:
            # Receive and print data
            data = client_socket.recv(1024)
            if not data:
                break
            print(data.decode('utf-8'))

            # Read data from input and send it
            response = input("Enter data to send: ")
            client_socket.sendall(response.encode('utf-8'))

        # Close the client socket when done
        client_socket.close()

if __name__ == "__main__":
    main()
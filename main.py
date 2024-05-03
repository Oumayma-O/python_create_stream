import socket
import time
import csv

def generate_data(csv_reader):
    # Read a row from the CSV file
    try:
        data = next(csv_reader)
        return ','.join(data)
    except StopIteration:
        return None

def main():
    port = 9999  # Port number to listen on

    # Start a socket server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('172.27.145.119', port))  
    server_socket.listen(1)

    print(f"Listening on port {port}")
    client_socket, address = server_socket.accept()
    print(f"Connection from {address}")

    # Open the CSV file
    with open('customer_data.csv', 'r') as file:
        csv_reader = csv.reader(file)
        try:
            while True:
                # Generate and send simulated streaming data
                data = generate_data(csv_reader)
                if data is not None:
                    client_socket.sendall(data.encode('utf-8'))
                    time.sleep(1)  # Simulate data being generated every second
                else:
                    break
        finally:
            # Close the sockets when done
            client_socket.close()
            server_socket.close()

if __name__ == "__main__":
    main()
import socket

def client_program():
    host = '127.0.0.1'  # server's hostname or IP address
    port = 65432        # server's port to connect to

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}.")

    while True:
        message = input("Enter message to send to server (type 'exit' to close): ")
        if message.lower() == 'exit':
            break

        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        print(f"Received from server: {data}")

    client_socket.close()
    print("Connection closed.")

if __name__ == "__main__":
    client_program()


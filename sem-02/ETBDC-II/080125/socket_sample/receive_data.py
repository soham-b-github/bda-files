import socket

def server_program():
    host = '127.0.0.1'  # localhost
    port = 65432        # port to listen on (above 1024 and below 65535)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}...")

    conn, address = server_socket.accept()
    print(f"Connection from {address} established.")
    
    while True:
        data = conn.recv(1024).decode()  # buffer size is 1024 bytes
        if not data:
            break
        print(f"Received from client: {data}")
        conn.send(data.encode())  # echo back the data
        print(f"Echoed back to client: {data}")

    conn.close()
    print("Connection closed.")

if __name__ == "__main__":
    server_program()


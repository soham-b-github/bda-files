# Streaming client
import socket

def streaming_client():
    host = '127.0.0.1'
    port = 65432

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to streaming server at {host}:{port}.")

    try:
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print(f"Received: {data}")
    finally:
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    streaming_client()


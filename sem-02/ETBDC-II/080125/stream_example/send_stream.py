# Streaming server
import socket
import time

def streaming_server():
    host = '127.0.0.1'
    port = 65432

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server streaming on {host}:{port}...")

    conn, address = server_socket.accept()
    print(f"Connection from {address} established.")
    
    try:
        for i in range(100):  # Stream 100 messages
            message = f"Streaming data {i}"
            conn.send(message.encode())
            time.sleep(0.5)  # Simulate real-time streaming
    finally:
        conn.close()
        print("Connection closed.")

if __name__ == "__main__":
    streaming_server()


import socket


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 12345)

    try:
        server_socket.bind(server_address)
        server_socket.listen(1)
        print("Server is waiting for connections...")

        client_socket, client_address = server_socket.accept()
        print(f"Connected to {client_address}")

        while True:
            data = client_socket.recv(1024)
            if not data:
                break

            print(f"Client: {data.decode('utf-8')}")
            message = input("Server: ")
            client_socket.send(message.encode('utf-8'))
    except KeyboardInterrupt:
        pass  # Gracefully exit on Ctrl+C
    finally:
        client_socket.close()
        server_socket.close()
        print("Server has exited.")



start_server()

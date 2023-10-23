import socket


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 12345)

    try:
        client_socket.connect(server_address)
        print("Connected to the server.")

        while True:
            message = input("Client: ")
            client_socket.send(message.encode('utf-8'))
            if message.lower() == "exit":
                break

            data = client_socket.recv(1024)
            print(f"Server: {data.decode('utf-8')}")
    except ConnectionRefusedError:
        print("Connection to the server failed.")
    except KeyboardInterrupt:
        pass  # Gracefully exit on Ctrl+C

    client_socket.close()
    print("Client has exited.")


start_client()

import threading


from config import *


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = set()
clients_lock = threading.Lock()


def handle_client(conn, adr):
    print(f"New member {adr} joined")

    try:
        connected = True
        while connected:
            msg = conn.recv(1024).decode(FORMAT)
            if not msg:
                break
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"{adr} > {msg}")
            with clients_lock:
                for client in clients:
                    client.sendall(f"{adr} > {msg}".encode(FORMAT))

    finally:
        with clients_lock:
            clients.remove(conn)
        conn.close()


def start():
    print("SERVER RUNNING")
    server.listen()
    while True:
        conn, adr = server.accept()
        with clients_lock:
            clients.add(conn)
        thread = threading.Thread(target=handle_client, args=(conn, adr))
        thread.start()


start()

from config import *


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client


def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)


def start():
    answer = input("Type 'go' to connect: ")
    if answer.lower() != "go":
        return

    connection = connect()
    while True:
        msg = input("Message (e for exit): ")

        if msg == "e":
            break

        send(connection, msg)

    send(connection, DISCONNECT_MESSAGE)


start()

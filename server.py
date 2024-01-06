import socket
import sys
import threading

host = '172.31.100.99'
port = '42069'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
clients = []
aliases = []

def broadcast_message(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast_message(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast_message(f"{alias} has left the chatroom.".encode('utf-8'))
            alias.remove(alias)
            break
def receive():
    while True:
        print('Server is running and listening...')
        client, address = server.accept()
        print(f'Connection is established with {str(address)}')
        client.send("Alias?".encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f"The alias of this client is {alias}".encode('utf-8'))
        broadcast_message(f"{alias} has connected to the chat room.".encode('utf-8'))

def main():
    try:
        s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #                               IPv4       TCP Protocol
        print("Socket Successfully Created.")
    except socket.error as err:
        print(f"ERROR: socket creation failure. {err}")
        return

    port = 42069
    s_sock.bind(('', port))
    print(f"Socket binded to port {port}.")
    s_sock.listen(3)
    print("Socket is listening...")
    while True:
        c, address = s_sock.accept()
        print("Received connection from", address)
        message = ('Thank you for connecting')
        c.send(message.encode())
        c.close()
if __name__ == '__main__':
    main()
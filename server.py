import socket
import threading

class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        self.clients = []
        self.aliases = []

    def broadcast(self, message):
        for client in self.clients:
            client.send(message)

    def handle_client(self, client):
        while True:
            try:
                message = client.recv(1024)
                self.broadcast(message)
            except:
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                alias = self.aliases[index]
                self.broadcast(f'{alias} has left the chat room!'.encode('utf-8'))
                self.aliases.remove(alias)
                break

    def receive(self):
        while True:
            print('Server is running and listening...')
            client, address = self.server.accept()
            print(f'Connection is established with {str(address)}')
            client.send('alias?'.encode('utf-8'))
            alias = client.recv(1024).decode('utf-8')
            self.aliases.append(alias)
            self.clients.append(client)
            print(f'The alias of this client is {alias}')
            
            # Broadcast a cleaner connection message
            connection_message = f" '{alias}' has connected to the chat room\n"
            self.broadcast(connection_message.encode('utf-8'))

            client.send('You are now connected!'.encode('utf-8'))
            thread = threading.Thread(target= self.handle_client, args=(client,))
            thread.start()
        


if __name__ == "__main__":
    chat_server = ChatServer('127.0.0.1', 59000)
    chat_server.receive()

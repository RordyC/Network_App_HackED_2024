import threading
import socket

class ChatClient:
    def __init__(self, host, port):
        self.alias = input('NAME: >>> ')
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.client.send(self.alias.encode('utf-8'))

        self.receive_thread = threading.Thread(target=self.receive_message)
        self.send_thread = threading.Thread(target=self.send_message)

    def start(self):
        self.receive_thread.start()
        self.send_thread.start()

    def receive_message(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if message == "alias?":
                    self.client.send(self.alias.encode('utf-8'))
                else:
                    print(message)
            except:
                print('Error!')
                self.client.close()
                break

    def send_message(self):
        while True:
            message = f'{self.alias}: {input("")}'
            self.client.send(message.encode('utf-8'))

if __name__ == "__main__":
    chat_client = ChatClient('127.0.0.1', 59000)
    chat_client.start()

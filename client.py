import threading
import socket
import tkinter as tk


class ChatClient:
    def __init__(self, host, port):
        self.alias = input('NAME: >>> ')
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.client.send(self.alias.encode('utf-8'))

        self.root = tk.Tk()
        self.root.title('Chat Client')

        self.chat_box = tk.Text(self.root, height=50, width=50)
        self.chat_box.pack()

        self.message_entry = tk.Entry(self.root, width=50)
        self.message_entry.pack()

        self.send_button = tk.Button(self.root, text='Send', command=self.send_message)
        self.send_button.pack()

        self.receive_thread = threading.Thread(target=self.receive_message)
        self.receive_thread.start()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def start(self):
        self.root.mainloop()

    def receive_message(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                self.chat_box.insert(tk.END, message + '\n')
            except:
                print('Error!')
                self.client.close()
                break

    def send_message(self):
        message = f'{self.alias}: {self.message_entry.get()}'
        self.client.send(message.encode('utf-8'))
        self.message_entry.delete(0, tk.END)

    def on_closing(self):
        self.client.close()
        self.root.destroy()

if __name__ == "__main__":
    chat_client = ChatClient('127.0.0.1', 59000)
    chat_client.start()

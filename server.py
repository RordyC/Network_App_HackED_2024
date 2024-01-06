import asyncio
import websockets

class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    async def handle_client(self, websocket, path):
        try:
            while True:
                message = await websocket.recv()
                print(f"Received message: {message}")
                await websocket.send(f"Echo: {message}")
        except websockets.exceptions.ConnectionClosedError:
            print("Connection closed")

    def start(self):
        start_server = websockets.serve(self.handle_client, self.host, self.port)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    chat_server = ChatServer("localhost", 8001)
    chat_server.start()

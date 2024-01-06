import asyncio
import websockets

async def send_message():
    uri = "ws://localhost:8001"
    async with websockets.connect(uri) as websocket:
        while True:
            message = input("Enter message: ")
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Server response: {response}")

asyncio.get_event_loop().run_until_complete(send_message())
#just trying to get the structure up

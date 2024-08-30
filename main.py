import asyncio
from websockets.asyncio.server import serve


async def handler(websocket):
    while True:
        message = await websocket.recv()
        print(message)
        await websocket.send("a")


async def main():
    async with serve(handler, "", 8001):
        await asyncio.get_running_loop().create_future()  # run forever

def setup():
    

if __name__ == "__main__":
    asyncio.run(main())
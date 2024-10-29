import asyncio
import websockets



async def handleConnection(websockets, path):
    print("Conectado")

    msn =await websockets.recv()
    print(msn)

async def startServer():
    async with websockets.serve(handleConnection, "10.80.7.55", 8765):
        print("Servidor run panananaan")
        await asyncio.Future()


asyncio.run(startServer())

#
import asyncio
import websockets



async def comunicateServer():
    ip ="ws://10.80.5.57:8765"
    async with websockets.connect(ip) as websoceckt:
        print("Conectado")
        msg ="Neurismene é a melhor"
        await websoceckt.send(msg)
    
    
    
 


asyncio.run(comunicateServer())
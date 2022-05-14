#!/usr/bin/env python
import asyncio
import websockets
import cv2
import numpy as np
import sys
import struct
import pickle


cap = cv2.VideoCapture(0)


async def handler(websocket, path):
    
    name = await websocket.recv()
    print("< {}".format(name))
    while True:
        #serializing the frame
        ret, frame= cap.read()
        data = pickle.dumps(frame)
        await websocket.send(data)


    #name = await websocket.recv()
    #print("< {}".format(name))

    #greeting = "Hello {}!".format(name)
    #await websocket.send(greeting)
    #print("> {}".format(greeting))
async def main():
    start_server = websockets.serve(handler, 'localhost', 8765)
    async with start_server:
        await asyncio.Future()

#asyncio.get_event_loop().run_until_complete(start_server)
#asyncio.get_event_loop().run_forever()
asyncio.run(main())
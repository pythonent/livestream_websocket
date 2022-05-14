#!/usr/bin/env python
import asyncio
import websockets
import pickle
import struct
import cv2
import numpy as np
import sys


async def handler():
    async with websockets.connect('ws://localhost:8765') as websocket:
        name = input("What's your name? ")
        await websocket.send(name)
        print("> {}".format(name))
        while True:
            frame_data = await websocket.recv()
            frame= pickle.loads(frame_data)
            cv2.imshow('frame', frame)
            cv2.waitKey(1)

        #name = input("What's your name? ")
        #await websocket.send(name)
        #print("> {}".format(name))

        #greeting = await websocket.recv()
        #print("< {}".format(greeting))

#asyncio.get_event_loop().run_until_complete(handler())
asyncio.run(handler())
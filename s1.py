from pypresence import Presence
import time


def splatoone():
    while True:
        time.sleep(1)
        rpc = Presence("789927198945443870")
        rpc.connect()
        rpc.update(start=int(time.time()), details="Front End", large_image="frontend", state="Working on JS")
        print("running")


splatoone()
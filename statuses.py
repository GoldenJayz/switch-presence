from pypresence import Presence
import time


def splatoone():
    while True:
        time.sleep(1)
        rpc = Presence("772118793841410088")
        rpc.connect()
        rpc.update(start=int(time.time()), details="Splatoon 2", large_image="s2")
        print("running")


def smash():
    while True:
        time.sleep(1)
        rpc = Presence("772118793841410088")
        rpc.connect()
        rpc.update(start=int(time.time()), details="Super Smash Bros. Ultimate", large_image="smash")
        print("running")

def zelda():
    while True:
        time.sleep(1)
        rpc = Presence("772118793841410088")
        rpc.connect()
        rpc.update(start=int(time.time()), details="The Legend of Zelda: Breath of the Wild", large_image="zelda")
        print("running")


from pypresence import Presence
import time

while True:
    time.sleep(1)
    rpc = Presence("789841902731526185")
    rpc.connect()
    rpc.update(start=int(time.time()), details="Playing", large_image="age")
    print("Displaying")
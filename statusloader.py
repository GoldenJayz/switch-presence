import tkinter as tk
from tkinter import *
import statuses

root = Tk()
filename = None


root.title("Switch Presence")
photo = PhotoImage(file = "./switch.png")
root.iconphoto(False, photo)

def splatoon():
    statuses.splatoone()

def smashh():
    statuses.smash()

def zelda():
    statuses.zelda()

B = Button(root, text = 'Splatoon 2', bd = '5', command = splatoon)
B.pack() 

bruh = Button(root, text = "Smash", bd = 5, command=smashh)
bruh.pack()

boo = Button(root, text = "Zelda", bd = 5, command=zelda)
boo.pack()

root.mainloop()
# class and function to display rolls for geomancy calculator

from tkinter import *
from roll import *

class Cell:
    def __init__(self, frame, roll):
        self.roll = roll
        self.label = Label(frame, font="Calibri 12 bold", borderwidth=2, relief=SUNKEN, width=7, bg="#7c63c7") 
    
    def createLines(self):
        output = createDots(self.roll.red) + "\n" + createDots(self.roll.yellow) + "\n" + createDots(self.roll.blue) + "\n" + createDots(self.roll.green)
        self.label.config(text=output)

def createDots(val):
    if val == 0:
        return "*   *"
    elif val == 1:
        return "*"
    else:
        print("invalidRoll")
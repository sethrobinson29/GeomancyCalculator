# data structures, and methods for displaying geomantic figures and brief desctiptions of them

from cell import *
from tkinter import messagebox

# dict of figure names and rolls
figures = {
    "Via": Roll(1, 1, 1, 1), 
    "Caput Draconis": Roll(0, 1, 1, 1),
    "Puella": Roll(1, 0, 1, 1),
    "Fortuna Major": Roll(0, 0, 1, 1),
    "Puer": Roll(1, 1, 0, 1),
    "Acquisito": Roll(0, 1, 0, 1),
    "Carcer": Roll(1, 0, 0, 1),
    "Tristitia": Roll(0, 0, 0, 1),
    "Cauda Draconis": Roll(1, 1, 1, 0),
    "Conjunctio": Roll(0, 1, 1, 0),
    "Amissio": Roll(1, 0, 1, 0),
    "Albus": Roll(0, 0, 1, 0),
    "Foruna Minor": Roll(1, 1, 0, 0),
    "Rubeus": Roll(0, 1, 0, 0),
    "Laetitia": Roll(1, 0, 0, 0),
    "Populus": Roll(0, 0, 0, 0),
}

# class to display figures
class Figure:
    def __init__(self, frame, figure):
        self.figure = figure
        self.roll = figures[figure]
        self.frame = Frame(frame, bg="#6023a0", borderwidth=2)
        self.label = Label(self.frame, font="Calibri 10 bold", borderwidth=2, relief=GROOVE, width=15, bg="#7c63c7", fg="#dfdd57") 
        self.button = Button(self.frame, cursor="hand2", text=self.figure, bg="#6023a0", fg="#dfdd57", borderwidth=0, activebackground="#7c63c7")
    
    def createLines(self):
        # output = createDots(self.roll.red) + "\n" + createDots(self.roll.yellow) + "\n" + createDots(self.roll.blue) + "\n" + createDots(self.roll.green) + "\n" + self.figure
        output = createDots(self.roll.red) + "\n" + createDots(self.roll.yellow) + "\n" + createDots(self.roll.blue) + "\n" + createDots(self.roll.green)
        self.label.config(text=output)

# descriptions of geomancy figures
descriptions = {
    "Via": "the Way\n\nVia represents change, solitude, and growth. This symbol is negative is stability is desired, but positive for change.",
    "Caput Draconis": "the Dragon's Head\n\nCaput Draconis indicates beginning, opportunity, and innocence. This figure is reassuring, yet\ncautioning of that which the querent does not know.",
    "Puella": "the Girl\n\nPuella represents healing, intuition, nuturing, and wisdom. It is positive for passive energies and the immediate\nfuture, and negative for long-term goals and planning.",
    "Fortuna Major": "Major Fortune\n\nFortuna Major is a very positive figure, representing luck, protection, and success thanks to the\ndilligence of the querent. Strength, genorsity, and likability are also represented.",
    "Puer": "the Boy\n\nPuer represents activity, responsibility, and enthusiasm. A psoitive figure for aggression or love, a negative\nfigure for all other questions. Puer can represent, courage and also impulsiveness.",
    "Acquisito": "Gain\n\nAcquisito represents material gain and an end to physical struggles.",
    "Carcer": "the Prison\n\nCarcer represents limitation, isolation, and indecision. Positive in questions of stability and security,\nCarcer indicates the querent should be aware of their emotions.",
    "Tristitia": "the Sadness\n\nTristitia represents disappointment, grief, or loss. Not always negative, but usuall indicates a general\ndownward trajectory",
    "Cauda Draconis": "the Dragon's Tail\n\nCauda Draconis indicates the end, closure, and new challenges. Positive if endings are expected.",
    "Conjunctio": "the Union\n\nConjunctio reperesents union and harmony. Highly-positive yet encouraging caution and thoughtfulness.\nNegative for questions of solitude.",
    "Amissio": "the Loss\n\nAmissio represents illness, loss, and dificulty. Positive if loss is desired, but mostly negative.",
    "Albus": "the White\n\nAlbus represents balance, and spiritual growth. Mostly positive, indicating slow but steady progress.",
    "Foruna Minor": "Minor Fortune\n\nFortuna Minor represents success through dilligence over time, with the help of others.",
    "Rubeus": "the Red\n\nRubeus represents violence, danger, and passion. Mostly negative, unless aggression is desired. Indicates the\nquerent should slow down and consider their actions.",
    "Laetitia": "the Joy\n\nLaetitia represents joy, good fortune, and contentment. Highly=positive, indcating balance, knowledge, and\nupward movement. Can also represent change and uprooting.",
    "Populus": "the People\n\nPopulus represent the passive influences of one's surroundings. Mostly neutral, Populus represents the\nUniverse reflecting back what the querent puts into it.",
}

# close window
def quit(win):
    win.destroy()

# creates a toplevel box to display information about a geomantic figure
def getDescription(root, figure):
    # messagebox.showinfo(figure, descriptions[figure])
    win = Toplevel(root, bg="#7c63c7")
    win.title(figure.figure)
    win.geometry("320x320")
    win.resizable(0,0)
    win.grab_set()

    topFrame = Frame(win, bg="#6023a0")
    topFrame.pack(padx=25, pady=15)

    # draw figure
    newFigure = figure
    newFigure.label = Label(topFrame, font="Calibri 14 bold", borderwidth=2, relief=RAISED, bg="#7c63c7", fg="#dfdd57") 
    newFigure.createLines() 
    newFigure.label.grid(column=0, row=0, ipadx=15, pady=4)
    
    # figure desription
    labelText = figure.figure +", " + descriptions[figure.figure]
    desc = Label(topFrame, font="Calibri 10 bold", relief=RAISED, text=labelText, wraplength=250, bg="#7c63c7") 
    desc.grid(column=0, row=1, padx=10)

    close = Button(topFrame, text="Close", cursor="hand2", command=lambda: quit(win), bg="#dfdd57", font=("Times New Roman", 12))
    close.grid(column=0, row=2, pady=10)

    
    win.mainloop()


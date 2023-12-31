# 
# Author: Seth Robinson
# Program: 4
# Date: July 14, 2023
# Description: A calculator for geomantic divination. Displays figures cast and sum of dots from chart. Includes brief explaination of geomancy and figures.
#  

from figures import *

# fills array with rolls and displays rolls as cells in a geomancy chart
def displayChart():
    rolls = []
    generateRolls(rolls)
    generateChart(rolls)
    cells = [Cell(chartFrame, roll) for roll in rolls]

    # create lines for all cells, fill chart frame with first 12
    temp = 6
    for i in range(15):
        cells[i].createLines()
        if i < 8:
            cells[i].label.grid(column=7-i, row=0, ipady=2, ipadx=4)
        elif i < 12:
            cells[i].label.grid(column=temp, row=1, columnspan=2, ipady=2, ipadx=7)
            cells[i].label.config(width=15)
            temp -= 2

    # fit rest of cells into frame
    cells[12].label.grid(column=4, row=2, columnspan=4, ipady=2, ipadx=17)
    cells[12].label.config(width=30)
    cells[13].label.grid(column=0, row=2, columnspan=4, ipady=2, ipadx=17)
    cells[13].label.config(width=30)
    cells[14].label.grid(column=0, row=3, columnspan=8, ipady=2, ipadx=37)
    cells[14].label.config(width=60)

    calcSum(rolls)

# translate values of rolls for sum calculation
def translateRoll(val):
    return 2 if val == 0 else 1

# calc sum of dots
def calcSum(rolls):
    res = 0
    for roll in rolls:
        res += translateRoll(roll.red)
        res += translateRoll(roll.yellow)
        res += translateRoll(roll.blue)
        res += translateRoll(roll.green)

    sum.config(text=str(res))

# messagebox description of geomancy 
def displayInfo():
    output = """\t********GEOMANCY CALCULATOR********
            \t\tBy Seth Robinson\n
Geomancy is a method of divination that interprets randomly generated markings or patterns, often made in the earth or 
from casting stones. Geomancy is thought to have started in the Middle East where it first spread to Greece. However,
modern geomancy was refined to the form shown in this calculator in the 19th century. For a more in-depth look at
geomancy, visit https://www.princeton.edu/~ezb/geomancy/geostep.html \n
GEOMANTIC FIGURES
Each geomantic figure, shown on the sides of the application, is made up of four lines. From top-to-bottom, the lines are:
fire (red), air (yellow), water (blue), earth (green). Each figure has a set of ideas and concepts associated with it, and
interpretation is largely up to the reader. This application works by generating a random number and creating a number
of dots based on that number (0 = 2 dots, 1 = 1 dot). To learn
more about a specific geomantic figure, click the name
underneath the corresponding figure.\n
GEOMANCY CHART
Charts are generated by rolling four figures, known as the Mothers. These initial rolls are placed from right-to-left on the
chart and then used to generated the other figures on the chart. The next four figures follow the Mothers on the first
row and are known as the Daughters. They are formed by
taking matching lines from each Mother figure (first Daughter
will be all fire lines, second Daughter all air lines, etc).
Next come the Nieces, which are generated by combining the
two figures above it. For each line, if the total number of dots
between 2 figures is an even number, the corresponding
Niece gets two dots, if the number of dots is odd, the Niece
gets one dot. This process is repeated to create the next two
figures, known as Witnesses, and repeated once more for the
final figure, known as the Judge. The sum of the dots is also
calculated and compared to the sum of all 16 figures (96). If
the chart's sum is less than 96, the situation in question 
will quickly approach, while if it is over 96, the querent
may be waiting for a bit."""
    messagebox.showinfo("About", output)

# GUI LOGIC
root = Tk()
root.geometry("790x735")
root.config(bg="#000000")
root.title("Seth Robinson")
root.resizable(0, 0)

# border frames
colSpace1 = Frame(root, height=600, width=50)
colSpace2 = Frame(root, height=600, width=50)
colSpace1.grid(column=0, row=0, rowspan=3, stick="W")
colSpace2.grid(column=2, row=0, rowspan=3, sticky="E")

# create and insert border figures into column frames
borderFigures = []
index = 0
for name in figures:
    if index < 8:
        borderFigures.append(Figure(colSpace1, name))
    else:
        borderFigures.append(Figure(colSpace2, name))
    borderFigures[index].createLines()
    borderFigures[index].frame.grid(column=0, row=index)
    borderFigures[index].label.grid(column=0, row=0)
    borderFigures[index].button.focus()
    borderFigures[index].button.grid(row=1, column=0)
    index += 1

# configure buttons for figure information
borderFigures[0].button.config(command= lambda: getDescription(root, borderFigures[0]))
borderFigures[1].button.config(command= lambda: getDescription(root, borderFigures[1]))
borderFigures[2].button.config(command= lambda: getDescription(root, borderFigures[2]))
borderFigures[3].button.config(command= lambda: getDescription(root, borderFigures[3]))
borderFigures[4].button.config(command= lambda: getDescription(root, borderFigures[4]))
borderFigures[5].button.config(command= lambda: getDescription(root, borderFigures[5]))
borderFigures[6].button.config(command= lambda: getDescription(root, borderFigures[6]))
borderFigures[7].button.config(command= lambda: getDescription(root, borderFigures[7]))
borderFigures[8].button.config(command= lambda: getDescription(root, borderFigures[8]))
borderFigures[9].button.config(command= lambda: getDescription(root, borderFigures[9]))
borderFigures[10].button.config(command= lambda: getDescription(root, borderFigures[10]))
borderFigures[11].button.config(command= lambda: getDescription(root, borderFigures[11]))
borderFigures[12].button.config(command= lambda: getDescription(root, borderFigures[12]))
borderFigures[13].button.config(command= lambda: getDescription(root, borderFigures[13]))
borderFigures[14].button.config(command= lambda: getDescription(root, borderFigures[14]))
borderFigures[15].button.config(command= lambda: getDescription(root, borderFigures[15]))

# title 
title = Label(root, text="GEOMANCY CALCULATOR", font=("Times New Roman", 20), bg="#dfdd57")
title.grid(column=1, row=0, padx=25, ipady=10, ipadx=20)

# container for geomancy chart
chartFrame = Frame(root, bg="#7319ff", height=350, width=560)
chartFrame.grid(column=1, row=1)

# frame below chart
botFrame = Frame(root, bg="#000000")
botFrame.grid(column=1, row=2)

# buttons
buttonFrame = Frame(botFrame, bg="#6023a0")
buttonFrame.grid(column=0, row=0, padx=10)
roll = Button(buttonFrame, text="Roll Chart",font=("Times New Roman", 14), command=displayChart, bg="#dfdd57")
roll.grid(column=0, row=0, padx=5, ipadx=3, ipady=3, pady=10)

about = Button(buttonFrame, text="About", command=displayInfo, bg="#dfdd57", font=("Times New Roman", 14))
about.grid(column=1, row=0, padx=5)

quitButton = Button(buttonFrame, text="Quit", command=lambda: quit(root), bg="#dfdd57", font=("Times New Roman", 12))
quitButton.grid(column=0, row=1, pady=10, padx=5)

# displays sum of dots from chart
sumFrame = Frame(botFrame, bg="#000000")
sumFrame.grid(column=1, row=0, padx=20)

sumLabel = Label(sumFrame, text="SUM:", bg="#6023a0", font=("Times New Roman", 16))
sumLabel.grid(column=1, row=0)
sum = Label(sumFrame, text="0", bg="#6023a0", font=("Times New Roman", 16), fg="#dfdd57")
sum.grid(column=2, row=0)

if __name__ == "__main__":
    root.mainloop()
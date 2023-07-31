# class and functions for storing rolls for geomantic divintion
from random import randint

class Roll:
    def __init__(self, red = -1, yellow = -1, blue = -1, green = -1):
        self.red = red
        self.yellow = yellow
        self.blue = blue
        self.green = green

# 0 - 3 = mothers
# 4 - 7 = daughters
# 8 - 11 = nieces, 
# 12 - 13 = witnesses 
# 14 = judge
def generateRolls(rolls):
    for i in range(4):
        rolls.append(Roll(randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1)))

def generateChart(rolls):
    # daughters
    rolls.append(Roll(rolls[0].red, rolls[1].red, rolls[2].red, rolls[3].red))
    rolls.append(Roll(rolls[0].yellow, rolls[1].yellow, rolls[2].yellow, rolls[3].yellow))
    rolls.append(Roll(rolls[0].blue, rolls[1].blue, rolls[2].blue, rolls[3].blue))
    rolls.append(Roll(rolls[0].green, rolls[1].green, rolls[2].green, rolls[3].green))

    # nieces
    index = 0
    for i in range(4):
        red = (rolls[index].red + rolls[index+1].red) % 2 
        yellow = (rolls[index].yellow + rolls[index+1].yellow) % 2 
        blue = (rolls[index].blue + rolls[index+1].blue) % 2 
        green = (rolls[index].green + rolls[index+1].green) % 2 
        rolls.append(Roll(red, yellow, blue, green))

        index+=2
    
    # witnesses
    rolls.append(Roll(((rolls[8].red + rolls[9].red) % 2 ), 
                      ((rolls[8].yellow + rolls[9].yellow) % 2 ),
                      ((rolls[8].blue + rolls[9].blue) % 2 ),
                      ((rolls[8].green + rolls[9].green) % 2 )))
    
    rolls.append(Roll(((rolls[10].red + rolls[11].red) % 2 ), 
                      ((rolls[10].yellow + rolls[11].yellow) % 2 ),
                      ((rolls[10].blue + rolls[11].blue) % 2 ),
                      ((rolls[10].green + rolls[11].green) % 2 )))
    
    # judge
    rolls.append(Roll(((rolls[12].red + rolls[13].red) % 2 ), 
                      ((rolls[12].yellow + rolls[13].yellow) % 2 ),
                      ((rolls[12].blue + rolls[13].blue) % 2 ),
                      ((rolls[12].green + rolls[13].green) % 2 )))

# prints single rolls values
def printRoll(roll):
        print(roll.red, roll.yellow, roll.blue, roll.green)

# prints list of rolls and index
def printRolls(rolls):
    line = 1
    for roll in rolls:
        print(line, roll.red, roll.yellow, roll.blue, roll.green)
        line += 1

#Alicia Williams
#CIS-125 FA 2015
#Week 6 Assignment
#File: GameofLife.py

import random

world = []
height = 80
width = 22


#Function Populate
#Precondtiitons
#world is  list

#Postconditions
#world will contain random cells
def populate(stuff, h = height, w = width):
    for x in range(h):
        row = []
        for y in range(w):
            row.append(random.randint(0,1))
        stuff.append(row)

#Function display
#Precondition
#   world is populated
#postcondition none
def display(cheese, h = height, w = width):
    worldString = ""
    for x in range(h):
        rowString = ""
        for y in range(w):
            if cheese[x][y] == 0:
                rowString += " "
            else:
                rowString += "*"
        worldString += rowString + "\n"
        print(worldString)
            
#Alicia Williams
#CIS-125 FA 2015
#Week 6 Assignment
#File: GameofLife.py
#Code that creates the framework of the Game of Life
#shown last week Friday
#Collaborated with Rebekah Orth and Dr. Neumann

def populate(world, h, w):
    pass
def display(world, h, w):
    pass
def generation(world, h, w):
    pass

def main():
    import random
    world = []
    h = 80
    w = 22
    
    populate(world, h, w)
    
    x = input("Press any key; press q to quit. ")
    while x != "q":
        display(world, h, w)
        generation(world, h, w)
        x = input("Press any key; press q to quit. ")

main()
    
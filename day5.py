import numpy as np

"""
Advent of Code 2022 - Day 5

Notes:
wow, lot of code this time. Parsing could be cut down quite ab it using divisions of the line length,
and later with regex. Probably worth praciticing regex more. Faster solutions used a lot of clever slicing
too.

Def need to work on more compact parsing, this would be good input data for practice

Time taken: ~20 min

"""

with open("day5.txt", "r") as file:
    inp = file.read().split("\n")

def getLetters(line):
    """
    From a line, extract the letters from the line
    returns in format ["", "", "", "A", "B"], where "" are empty spots
    
    """
    letters = []
    spl = line.replace("    ", "-").replace(" ", "-").split("-")
    for item in spl:
        if item == "":
            letters.append("")
        elif item[0] == "[":
            letters.append(item[1])
        else:
            pass
    return letters


table = []
inst_index = 0
for i, line in enumerate(inp):
    table.append(getLetters(line)) #append to table the letters 
    if len(line) == 0: #check for when weve reached the end of the table
        del table[-1] #and remove the extra entries
        del table[-1]
        inst_index = i+1 #record the index the instructions begin 
        break

table = np.transpose(table) #transpose to get it to be a list of stacks
stacks = [] # here I realized how convienent stack data structures would be, so quick  
            # reorganization of data into stacks without blank spaces
            # would've been better to do this from the start but oh well
for i, stack in enumerate(table):
    stacks.append([])
    for item in stack:
        if item != "":
            stacks[i].append(item)
    stacks[i].reverse() #since we append from top down, reverse so our top elements are at the 
                        #end of the stack

#part 2
def makeMove_p2(n, s1, s2): #make a move, move n crates from s1 to s2, order maintained
    int_stack = []
    for i in range(0, n):
        int_stack.append(stacks[s1-1].pop())
    for i in range(0, n):
        stacks[s2-1].append(int_stack.pop())

#part 1
def makeMove_p1(n, s1, s2): #make a move, move n crates from s1 to s2, order not maintaned
    for i in range(0, n):
        stacks[s2-1].append(stacks[s1-1].pop())


for i in range(inst_index, len(inp)): #carry out move for each instruction
    line = inp[i]
    line = line.split(" ")
    n =  int(line[1] )
    s1 = int(line[3])
    s2 = int(line[5])
    
    makeMove_p2(n, s1, s2)

#print top item for each stack
for stack in stacks:
    print(stack.pop(), end="")




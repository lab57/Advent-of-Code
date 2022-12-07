from utils import *
"""
Advent of Code 2022 - Day 7

Notes: This one was a long one
Couldve been made substancially shorter by making some observations/assumptions about the input data,
mainly that each dir will be ls'd exactly once.

I think using match statements couldve pretty greately simplified the parsing code - maybe will redo using it.


Time: ~30 min 
"""


with open("day7.txt", "r") as file:
    inp = file.read().split("\n")
OUT = inp 


# Folder class, almost like a tree
class Folder:
    def __init__(self, name) -> None:
        pass
        self.name = name
        self.size = 0
        self.children = {}
        self.files = {}
        self.parent = None

    def addSize(self, val):
        # Adds data size to itself and to its parents
        self.size += val
        if self.parent:
            self.parent.addSize(val)
    
    #convienence
    def __eq__(self, __o: object) -> bool:
        if type(__o) == str:
            return self.name == __o
        else:
            return self.name == __o.name
    def __repr__(self) -> str:
        return f"{self.name} - {self.size}"
    
root = None
currentFolder = None
allFolders = [] #for convienence to avoid having to navigate like a tree
for i, line in enumerate(inp):
    if line[0] == "$": #user command
        pts = line.split(" ") #parts
        if pts[1] == "cd": #command is cd
            arg = pts[2]
            if arg == "..": #parent
                currentFolder = currentFolder.parent

            elif currentFolder is None: #special case, create root
                currentFolder = Folder(arg)
                root = currentFolder
                allFolders.append(root)

            else: #'normal case', cd into existing folder (folders must be seen by ls before we cd into them)
                currentFolder = currentFolder.children[arg]


        if pts[1] == "ls": #ls command

            for lin in inp[i+1:]: #from current line to the endish
                if(lin[0] == "$"): #reached end of ls output
                    break
                args = lin.split(" ")
                if args[0] == "dir": #directory
                    if args[1] not in currentFolder.children.keys(): #check if not seen before, this is actually the only case (ls is run once per directory)
                        newFolder = Folder(args[1]) #create folder
                        newFolder.parent = currentFolder
                        currentFolder.children[args[1]] = newFolder

                        allFolders.append(newFolder) 

                    else: #we dont reach this branch
                        pass
                
                elif args[0].isnumeric(): #redundant check, just felt like adding
                    currentFolder.addSize(int(args[0])) #add the size of the file to the current folder and propagate above to the parents


print("Done parsing")


#find sum of folders under 100_000 in size
s = 0
for Folder in allFolders:
    if Folder.size <= 100_000:
        s += Folder.size
print(f"SUM: {s}")

#find smallest folder we can delete to make sufficient room
space = 70000000-root.size #space available on drive
allFolders.sort(key=lambda x: x.size)
for fol in allFolders:
    if space + fol.size >= 30000000:
        print("DELETE:", fol)
        break
    





from utils import *
"""
Advent of Code 2022 - Day 7 - Revised

Redid tihs one with match statements and some other assumptions. 
Not a ton shorter but definitely more readable and cleaner.
Could probably be done much faster without folder class but i like it so oh well

"""


class Folder:
    """
    Folder class. No need to worry about folders children directorys as we always travel inwards,
    so any new file discoveries can be carried upwards.
    """
    def __init__(self, name, parent) -> None:
        pass
        self.name = name
        self.size = 0
        self.parent = parent

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

with open("day7.txt", "r") as file:
    inp = file.read().split("\n")


i = 0
root = None
currentFolder = None
allFolders = []
while i < len(inp):
    match inp[i].split():
        case ['$', 'ls']: #ls command
            while i+1 < len(inp) and inp[i+1][0] != "$": #while next i is valid and not a new command
                i+= 1
                match inp[i].split():
                    case ["dir", name]: #folder, we assume each folder will be cd'd so we dont need
                                        #need to take action
                        pass
                    case [size, name]: #file with a size. No need to keep track of files, just the sizes
                        currentFolder.addSize(int(size))
            pass 
        case ['$', 'cd', arg]: #assume we cd each folder once, we will cd folder before lsing it
            match arg: 
                case "..": #parent
                    currentFolder = currentFolder.parent
                case name: #folder
                    newFolder = Folder(name, currentFolder)
                    allFolders.append(newFolder)

                    if currentFolder is None: #root directoty
                        root = newFolder

                    currentFolder = newFolder       
    i+=1
print("Done parsing")
s = 0
for fol in allFolders:
    if fol.size <= 100_000:
        s += fol.size
print(f"SUM: {s}")

#find smallest folder we can delete to make sufficient room
space = 70000000-root.size #space available on drive
allFolders.sort(key=lambda x: x.size)
for fol in allFolders:
    if space + fol.size >= 30000000:
        print("DELETE:", fol)
        break
    

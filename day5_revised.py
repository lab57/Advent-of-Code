import numpy as np

inp = open("day5.txt")


letters = []
for line in inp:
    if line == "\n":
        del letters[-1]
        break
    letters.append(line[1::4])

print(letters)

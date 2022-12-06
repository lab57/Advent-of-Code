from utils import *

"""
Advent of Code 2022 - Day 6

Notes:
None his time, went pretty good tbh

Time: ~4 min
"""

with open("day6.txt", "r") as file:
    inp = file.read()

n = 4  # size of window
for i in range(len(inp)):
    sub = inp[i : i + n]  # slice to the size of the window
    if len(set(sub)) == n:  # cast to a set and see if its the same size of the window
        print(f"Found, {i + n}")  # if so, found our index (offset by n)
        break

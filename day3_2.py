"""
Advent of Code 2022 - Day 3 - Part 2

"""


with open("day3.txt", "r") as file:
    input = file.read().split("\n")




def getPriority(letter):
    return ord(letter)-ord("a")+1 if letter.islower() else ord(letter)-ord("A")+27


score = 0
for i in range(0, len(input),3):
    for letter in input[i]:
        if letter in input[i+1] and letter in input[i+2]:
            score += getPriority(letter)
            break
print(score)
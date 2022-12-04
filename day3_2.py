"""
Advent of Code 2022 - Day 3 - Part 2

"""


with open("day3.txt", "r") as file:
    input = file.read().split("\n")




def getPriority(letter):
    """
    Calculate the priority of a letter char
    
    """
    return ord(letter)-ord("a")+1 if letter.islower() else ord(letter)-ord("A")+27


score = 0
for i in range(0, len(input),3): #skip over the input indicies in steps of 3
    for letter in input[i]:
        if letter in input[i+1] and letter in input[i+2]: #check if letter in both sacks
            score += getPriority(letter)
            break
print(score)
"""
Advent of Code 2022 - Day 3

"""


with open("day3.txt", "r") as file:
    input = file.read().split("\n")


input = [(sack[0:len(sack)//2], sack[len(sack)//2:]) for sack in input]


def getPriority(letter):
    return ord(letter)-ord("a")+1 if letter.islower() else ord(letter)-ord("A")+27


score = 0

for sack in input:
    print(sack)
    for letter in sack[0]:
        if letter in sack[1]:
                score += getPriority(letter)
                break
print(score)


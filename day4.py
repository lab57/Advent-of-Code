"""
Advent of Code 2022 - Day 4

Notes:
Time: ~6 minutes
map() is useful, worth praciting. Couldve killed lines 14-18 and simplifed the rest

"""
with open("day4.txt", "r") as file:
    input = file.read().split("\n")

contained = 0
for line in input:
    #split into groups of ints for each elf
    split1 = line.split(",")
    elf1 = split1[0].split("-")
    elf2 = split1[1].split("-")
    elf1 = [int(elf1[0]), int(elf1[1])]
    elf2 = [int(elf2[0]), int(elf2[1])]

    #check if both values for elf2 are contained in elf1, and vice versa
    #change the ors to ands for part 1
    if elf1[0] <= elf2[0] <= elf1[1] or elf1[0] <= elf2[1] <= elf1[1]:
        contained += 1
    elif elf2[0] <= elf1[0] <= elf2[1] or elf2[0] <= elf1[1] <= elf2[1]:
        contained += 1
print(contained)






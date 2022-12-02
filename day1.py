with open("day1.txt", "r") as file:
    spl = file.read().split("\n\n")
values = []
for i, elf in enumerate(spl):
    cals = 0
    for item in elf.split("\n"):
        cals += int(item)
    values.append(cals)
values.sort(reverse=True)
print(f"Part 1: {values[0]}")
print(f"Part 2: {values[0] + values[1] + values[2]}")

with open("day2.txt", "r") as file:
    input = file.read().split("\n")

map = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2,
}
score = 0

for round in input:
    if map[round[0]] == map[round[2]]:
        score += 3
    if (map[round[2]] - map[round[0]]) % 3 == 1:
        score += 6
    score += map[round[2]] + 1

print(f"Part 1 {score}")


score = 0

for round in input:
    p1 = round[0]
    p2 = round[2]
    p2c = None  # player 2 choice
    if p2 == "X":  # loss
        p2c = (map[p1] - 1) % 3
    elif p2 == "Y":
        score += 3
        p2c = map[p1]
    elif p2 == "Z":
        score += 6
        p2c = (map[p1] + 1) % 3
    score += p2c + 1

print(f"Part 2 {score}")

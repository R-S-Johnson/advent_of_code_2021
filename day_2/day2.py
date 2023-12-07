sub = [0, 0, 0]

with open("day_2/input.txt", 'r') as f:
    data = f.readlines()
    data = [line.split(' ') for line in data]

for line in data:
    if line[0] == "forward":
        sub[0] += int(line[1])
        sub[1] += sub[2] * int(line[1])
    elif line[0] == "down":
        sub[2] += int(line[1])
    elif line[0] == "up":
        sub[2] -= int(line[1])

print(sub[0] * sub[1])
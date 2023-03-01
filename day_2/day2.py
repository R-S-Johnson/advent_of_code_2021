sub = [0, 0, 0]

file = open("day_2/input.txt", 'r')

for line in file.readlines():
    newLine = line.split()
    if newLine[0] == "forward":
        sub[0] += int(newLine[1])
        sub[1] += sub[2] * int(newLine[1])
    elif newLine[0] == "down":
        sub[2] += int(newLine[1])
    elif newLine[0] == "up":
        sub[2] -= int(newLine[1])

print(sub[0]*sub[1])
file.close()
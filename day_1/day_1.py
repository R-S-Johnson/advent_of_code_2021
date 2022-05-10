

f = open("day_1/input.txt", "r")
lines = f.readlines()

next = 1
current = 0
count = 0

for i in range(len(lines) - 3):
    if int(lines[current].strip()) + int(lines[current + 1].strip()) + int(lines[current + 2].strip()) < int(lines[next].strip()) + int(lines[next + 1].strip()) + int(lines[next + 2].strip()):
        count += 1
    next += 1
    current += 1

print(count)
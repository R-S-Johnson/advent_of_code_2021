

f = open("day_1/input.txt", "r")

next = int(f.readline().strip())
previous = None
count = 0

for line in f.readlines():
    previous = next
    next = int(line.strip())
    if previous < next:
        count += 1
print(count)
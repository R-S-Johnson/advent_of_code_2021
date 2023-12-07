

with open("day_1/input.txt", "r") as f:
    data = f.readlines()
    data = [int(i) for i in data]

count = 0

summ = [sum(data[(0+i):(3+i)]) for i in range(len(data)-2)]
prev = summ[0]

for elem in summ:
    if elem > prev:
        count += 1
    prev = elem

print(count)
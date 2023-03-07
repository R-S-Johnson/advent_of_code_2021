
def binToDec(bin):
    toreturn = 0
    power = 0
    for i in range(len(bin)-1, -1, -1):
        if bin[i] == 1:
            toreturn += 2 ** power
        power += 1
    return toreturn


file = open("day_3/input.txt", "r")

def part1():
    lines = file.readlines()
    output = [[0, 0] for i in range(len(lines[0].strip()))]

    for line in lines:
        for i in range(len(line.strip())):
            if line[i] == "1":
                output[i][1] += 1
            else:
                output[i][0] += 1

    gamma = [0 for i in range(len(output))]
    eps = [1 for i in range(len(output))]
    for i in range(len(gamma)):
        if output[i][1] > output[i][0]:
            gamma[i] = 1
            eps[i] = 0

oxy = []
co2 = []

lines = file.readlines()

output = [[0, 0] for i in range(len(lines[0].strip()))]

for line in lines:
    for i in range(len(line.strip())):
        if line[i] == "1":
            output[i][1] += 1
        else:
            output[i][0] += 1
    oxy.append(line.strip())
    co2.append(line.strip())


for bitIndex in range(len(oxy[0])):
    for wordIndex in range(len(oxy)):
        if output[wordIndex][0] > output[wordIndex][1]:
            if oxy[wordIndex][bitIndex] == "0":
                co2.remove(co2[wordIndex])
            else:
                oxy.remove(oxy[wordIndex])
    if len(oxy) == len(co2) == 1:
        break

print(oxy)
print(co2)
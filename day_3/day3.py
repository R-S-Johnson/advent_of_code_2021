
def binToDec(bin):
    toreturn = 0
    power = 0
    for i in range(len(bin)-1, -1, -1):
        if bin[i] == 1:
            toreturn += 2 ** power
        power += 1
    return toreturn


file = open("day_3/input.txt", "r")

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

print(binToDec(gamma) * binToDec(eps))


with open("day_3/input.txt") as f:
    data = [line.strip() for line in f.readlines()]

common = [0 for _ in range(len(data[0]))]
for i in range(len(common)):
    common[i] = round(sum([int(line[i]) for line in data])/len(data))

oxyGen = data.copy()
CO2Scrub = data.copy()

for i in range(len(common)):
    for num in data:
        if num[i] != common[i]:
            oxyGen.pop(i)
        else:
            CO2Scrub.pop(i)

print(oxyGen)
print(CO2Scrub)
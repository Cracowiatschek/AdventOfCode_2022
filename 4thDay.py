# Part 1

with open("4thDay.txt", "r") as file:
    lines = file.read().split("\n")

def commonMember(stList, ndList):
    result = [i for i in stList if i in ndList]
    return result

stElves = []
ndElves = []
elves = []

for i in lines:
    elf = i.split((","))
    elves.append(elf)

    splitStElf = elf[0].split('-')
    splitNdElf = elf[1].split('-')

    stElf = []
    ndElf = []

    for element in splitStElf:
        stElf.append(int(element))

    for element in splitNdElf:
        ndElf.append(int(element))

    stElves.append(stElf)
    ndElves.append(ndElf)

rangeStElves = []
rangeNdElves = []

for i in stElves:
    data = []
    for num in range(i[0],i[1]+1):
        data.append(num)

    rangeStElves.append(data)

for i in ndElves:
    data = []
    for num in range(i[0],i[1]+1):
        data.append(num)

    rangeNdElves.append(data)

data = []
id = 0

for i in range(len(rangeStElves)):
    score = commonMember(rangeStElves[id],rangeNdElves[id])
    if len(score) == len(rangeStElves[id]):
        data.append(score)
    elif len(score) == len(rangeNdElves[id]):
        data.append(score)
    else:
        pass

    id += 1

print(len(data))

# Part 2

data = []
id = 0

for i in range(len(rangeStElves)):
    score = commonMember(rangeStElves[id],rangeNdElves[id])
    if score != []:
        data.append(score)
    else:
        pass
    id += 1

print(len(data))
# Part One
with open("6thDay.txt", "r") as file:
    lines = file.read()

chars = list(lines)
result = []

id = 0

for i in range(len(chars)-4):
    section = chars[id:id+4]

    result.append(list(set(section)))
    id += 1

score = []

id = 0

for i in result:

    if len(i) == 4:
        score.append(id+4)
        id += 1
    else:
        id += 1

print('')
print('Part One Answer:' + str(min(score)))

#Part Two
result = []

id = 0

for i in range(len(chars)-14):
    section = chars[id:id+14]
    result.append(list(set(section)))
    id += 1

score = []

id = 0
for i in result:

    if len(i) == 14:
        score.append(id+14)
        id += 1
    else:
        id += 1

print('Part Two Answer:' + str(min(score)))

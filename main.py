
with open("5thDay.txt", "r") as file:
    lines = file.read().split("\n")[0:8]

with open("5thDay.txt", "r") as ins:
    instruction = ins.read().split("\n")[10:]

directions = []

for i in instruction:
    s = i.split(' ')
    directions.append([int(s[1]), int(s[3]), int(s[5])])

first = []
second = []
third = []
fourth = []
fifth = []
sixth = []
seventh = []
eighth = []
nineth = []


for i in lines:

    if i[1] != ' ':
        first.append(i[1])
    else:
        pass
    if i[5] != ' ':
        second.append(i[5])
    else:
        pass
    if i[9] != ' ':
        third.append(i[9])
    else:
        pass
    if i[13] != ' ':
        fourth.append(i[13])
    else:
        pass
    if i[17] != ' ':
        fifth.append(i[17])
    else:
        pass
    if i[21] != ' ':
        sixth.append(i[21])
    else:
        pass
    if i[25] != ' ':
        seventh.append(i[25])
    else:
        pass
    if i[29] != ' ':
        eighth.append(i[29])
    else:
        pass
    if i[33] != ' ':
        nineth.append(i[33])
    else:
        pass

print(directions[:3])
print(directions[-3:])
print('')

first.reverse()
second.reverse()
third.reverse()
fourth.reverse()
fifth.reverse()
sixth.reverse()
seventh.reverse()
eighth.reverse()
nineth.reverse()

print(first)
print(second)
print(third)
print(fourth)
print(fifth)
print(sixth)
print(seventh)
print(eighth)
print(nineth)
print(len(first)+len(second)+len(third)+len(fourth)+len(fifth)+len(sixth)+len(seventh)+
      len(eighth)+len(nineth))

def box(howMuch, toList, fromList):
    toList.extend(fromList[-howMuch:])
    del fromList[-howMuch:]
    return toList


for i in directions:
    boxes = [first, second, third, fourth, fifth, sixth, seventh, eighth, nineth]
    box(i[0],boxes[i[2]-1],boxes[i[1]-1])


print('')

print(first)
print(second)
print(third)
print(fourth)
print(fifth)
print(sixth)
print(seventh)
print(eighth)
print(nineth)
print(len(first)+len(second)+len(third)+len(fourth)+len(fifth)+len(sixth)+len(seventh)+
      len(eighth)+len(nineth))
print('Answer: ' + str(first[-1]) + str(second[-1]) + str(third[-1]) + str(fourth[-1]) +
                 str(fifth[-1]) + str(sixth[-1]) + str(seventh[-1]) + str(eighth[-1]) + str(nineth[-1]))


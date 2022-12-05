with open("5thDay.txt", "r") as file:
    lines = file.read().split("\n")[0:8]

with open("5thDay.txt", "r") as ins:
    instruction = ins.read().split("\n")[10:]

directions = []

for i in instruction:
    s = i.split(' ')
    directions.append([int(s[1]), int(s[3]), int(s[5])])

first = []
firstCopy = []
second = []
secondCopy = []
third = []
thirdCopy = []
fourth = []
fourthCopy = []
fifth = []
fifthCopy = []
sixth = []
sixthCopy = []
seventh = []
seventhCopy = []
eighth = []
eighthCopy =[]
nineth = []
ninethCopy = []

for i in lines:

    if i[1] != ' ':
        first.append(i[1])
        firstCopy.append(i[1])
    else:
        pass
    if i[5] != ' ':
        second.append(i[5])
        secondCopy.append(i[5])
    else:
        pass
    if i[9] != ' ':
        third.append(i[9])
        thirdCopy.append(i[9])
    else:
        pass
    if i[13] != ' ':
        fourth.append(i[13])
        fourthCopy.append(i[13])
    else:
        pass
    if i[17] != ' ':
        fifth.append(i[17])
        fifthCopy.append(i[17])
    else:
        pass
    if i[21] != ' ':
        sixth.append(i[21])
        sixthCopy.append(i[21])
    else:
        pass
    if i[25] != ' ':
        seventh.append(i[25])
        seventhCopy.append(i[25])
    else:
        pass
    if i[29] != ' ':
        eighth.append(i[29])
        eighthCopy.append(i[29])
    else:
        pass
    if i[33] != ' ':
        nineth.append(i[33])
        ninethCopy.append(i[33])
    else:
        pass

first.reverse()
firstCopy.reverse()
second.reverse()
secondCopy.reverse()
third.reverse()
thirdCopy.reverse()
fourth.reverse()
fourthCopy.reverse()
fifth.reverse()
fifthCopy.reverse()
sixth.reverse()
sixthCopy.reverse()
seventh.reverse()
seventhCopy.reverse()
eighth.reverse()
eighthCopy.reverse()
nineth.reverse()
ninethCopy.reverse()


def box(howMuch, toList, fromList):
    append = fromList[-howMuch:]
    append.reverse()
    toList.extend(append)
    del fromList[-howMuch:]
    return toList


for i in directions:
    boxes = [first, second, third, fourth, fifth, sixth, seventh, eighth, nineth]

print('')
print('Answer Part One: ' + str(first[-1]) + str(second[-1]) + str(third[-1]) + str(fourth[-1]) +
      str(fifth[-1]) + str(sixth[-1]) + str(seventh[-1]) + str(eighth[-1]) + str(nineth[-1]))
# Part Two

def boxNd(howMuch, toList, fromList):
    toList.extend(fromList[-howMuch:])
    del fromList[-howMuch:]
    return toList

for i in directions:
    boxes = [firstCopy, secondCopy, thirdCopy, fourthCopy, fifthCopy, sixthCopy, seventhCopy, eighthCopy, ninethCopy]
    boxNd(i[0], boxes[i[2] - 1], boxes[i[1] - 1])

print('Answer Part Two: ' + str(firstCopy[-1]) + str(secondCopy[-1]) + str(thirdCopy[-1]) + str(fourthCopy[-1]) +
    str(fifthCopy[-1]) + str(sixthCopy[-1]) + str(seventhCopy[-1]) + str(eighthCopy[-1]) + str(ninethCopy[-1]))

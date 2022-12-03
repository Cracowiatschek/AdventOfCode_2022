# Part 1
with open("2ndDay.txt", "r") as file:
    lines = file.read().split("\n")

#A - rock - X
#B - paper - Y
#C - scissors - Z

listOfWins = ['A Y', 'B Z', 'C X']
listOfDraws = ['A X', 'B Y', 'C Z']
listOfLosses = ['A Z', 'B X', 'C Y']

result = []


def search(list, param, points):
    for i in range(len(list)):
        if list[i] == param:
            result.append(points)


def points(listOfWins, listOfDraws, listOfLosses):
    for i in lines:
        search(listOfWins,i,6)

    for i in lines:
        search(listOfDraws,i,3)

    for i in lines:
        search(listOfLosses,i,0)

    for i in lines:
        if i[2:] == 'Z':
            result.append(3)
        elif i[2:] == 'Y':
            result.append(2)
        elif i[2:] == 'X':
            result.append(1)

points(listOfWins,listOfDraws,listOfLosses)

print(result)
print('')
print(sum(result))

# Part 2

wins = []
draws = []
losses = []
result_II = []

for i in lines:
    if i[2:] == 'Z':
        result_II.append(6)
        wins.append(i[:2])
    elif i[2:] == 'Y':
        result_II.append(3)
        draws.append(i[:2])
    elif i[2:] == 'X':
        result_II.append(0)
        losses.append(i[:2])

for points in wins:
    if points == 'A':
        result_II.append(2)
    elif points == 'B':
        result_II.append(3)
    elif points == 'C':
        result_II.append(1)

for points in draws:
    if points == 'A':
        result_II.append(2)
    elif points == 'B':
        result_II.append(3)
    elif points == 'C':
        result_II.append(1)

for points in losses:
    if points == 'A':
        result_II.append(2)
    elif points == 'B':
        result_II.append(3)
    elif points == 'C':
        result_II.append(1)


print(result_II)
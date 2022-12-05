# Part 1
with open("1stDay.txt", "r") as file:
    lines = file.read().split("\n")

calories = []

for i in lines:
    if i == '':
        a = 0
        calories.append(a)
    else:
        calories.append(int(i))

elves = []
cal = []

for c in calories:
    if c != 0:
        cal.append(c)
    elif c == 0:
        elves.append(sum(cal))
        cal = []
    else:
        pass

print(max(elves))

# Part 2
elves.sort()
long = len(elves)

top3 = [elves[-3:]]

print(sum(top3))

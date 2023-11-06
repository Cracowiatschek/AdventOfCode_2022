# part 1| *
file = open('input.txt', 'r').read().split('\n')

calories = []

for i in file:
    if i == '':
        a = 0
        calories.append(a)
    else:
        calories.append(int(i))

elves = []
kcal = []

for cal in calories:
    if cal != 0:
        kcal.append(cal)
    elif cal == 0:
        elves.append(sum(kcal))
        kcal = []
    else:
        continue

print(f'The Elf that has the most food gets \033[32m{max(elves)}\033[0m kcal\n')

# part two| **
elves.sort()

top3 = elves[-3:]

print(f'The three Elves carrying the most food carry \033[32m{sum(top3)}\033[0m kcal')

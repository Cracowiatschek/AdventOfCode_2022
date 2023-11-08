# part 1| *

file = open('input.txt', 'r').read().split('\n')

cycle = 0
x = 1
monitor = [20, 60, 100, 140, 180, 220]

result = 0

for line in file:
    operation = line.split(' ')
    for i in operation:
        cycle += 1
        if cycle in monitor:
            result += cycle * x
        else:
            continue
    if len(operation) == 2:
        x += int(operation[1])
    else:
        continue

print(f"Sum of signal strenght is \033[32m{result}\033[0m")
# part 2| **
cycle = 0
x = 1
x_pos = []
pos = 0

for line in file:
    operation = line.split(' ')
    for i in operation:
        cycle += 1
        x_pos.append(x)
    if len(operation) == 2:
        x += int(operation[1])
    else:
        continue

result = []
row = []
px = 40

for n in range(int(cycle/px)):
    for x in range(px):
        cnt = n * px + x
        if abs(x_pos[cnt] - x) <= 1:
            row.append('##')
        else:
            row.append('XX')

        if len(row) == px:
            result.append(row)
            row = []
        else:
            continue

print("My solution: ")
for row in result:
    view = ""
    for n in row:
        if n == '##':
            view += f'\033[31m{n}\033[0m'
        else:
            view += n
    print(view)

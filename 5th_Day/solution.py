# part 1| *
stacks_base = open('input.txt', 'r').read().split('\n')[0:8]
instructions = open('input.txt', 'r').read().split('\n')[10:]

directions = []

for i in instructions:
    instruction = i.split(' ')
    directions.append([int(instruction[1]), int(instruction[3]), int(instruction[5])])

stacks = [[i[1] for i in stacks_base], [i[5] for i in stacks_base], [i[9] for i in stacks_base],
          [i[13] for i in stacks_base], [i[17] for i in stacks_base], [i[21] for i in stacks_base],
          [i[25] for i in stacks_base], [i[29] for i in stacks_base], [i[33] for i in stacks_base]]

for i in stacks:
    i.reverse()
    cnt = i.count(' ')
    if cnt != 0:
        del i[-cnt:]
    else:
        continue

for i in directions:
    boxes = i[0]
    from_stack = i[1]
    to_stack = i[2]
    elevator = stacks[from_stack - 1][-boxes:]
    elevator.reverse()
    stacks[to_stack - 1].extend(elevator)
    del stacks[from_stack - 1][-boxes:]

result = [i[-1] for i in stacks]

print(f'The top boxes of towers is \033[32m{result}\033[0m \n')

# part 2| **
stacks = [[i[1] for i in stacks_base], [i[5] for i in stacks_base], [i[9] for i in stacks_base],
          [i[13] for i in stacks_base], [i[17] for i in stacks_base], [i[21] for i in stacks_base],
          [i[25] for i in stacks_base], [i[29] for i in stacks_base], [i[33] for i in stacks_base]]

for i in stacks:
    i.reverse()
    cnt = i.count(' ')
    if cnt != 0:
        del i[-cnt:]
    else:
        continue

for i in directions:
    boxes = i[0]
    from_stack = i[1]
    to_stack = i[2]
    elevator = stacks[from_stack - 1][-boxes:]
    stacks[to_stack - 1].extend(elevator)
    del stacks[from_stack - 1][-boxes:]

result = [i[-1] for i in stacks]

print(f'The top boxes of towers is \033[32m{result}\033[0m')

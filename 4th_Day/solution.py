# part 1| *

file = open('input.txt', 'r').read().split('\n')


def common_member(st_list, nd_list):
    result = [i for i in st_list if i in nd_list]
    return result


elves = []

for lines in file:
    pair = []
    elf = lines.split(',')
    st_elf = elf[0].split('-')
    st_elf = range(int(st_elf[0]), int(st_elf[1]) + 1)
    pair.append(st_elf)

    nd_elf = elf[1].split('-')
    nd_elf = range(int(nd_elf[0]), int(nd_elf[1]) + 1)
    pair.append(nd_elf)
    elves.append(pair)

summary = []

for elf in elves:
    rng_st_elf = len(elf[0])
    rng_nd_elf = len(elf[1])
    score = common_member(elf[0], elf[1])
    if len(score) == rng_nd_elf or len(score) == rng_st_elf:
        summary.append(score)
    else:
        continue

print(f'The number of pairs that fully overlap: \033[32m{len(summary)}\033[0m \n')

# part 2| **
summary = []

for elf in elves:
    score = common_member(elf[0], elf[1])
    if len(score) != 0:
        summary.append(score)
    else:
        continue

print(f'The number of pairs that partly overlap: \033[32m{len(summary)}\033[0m \n')

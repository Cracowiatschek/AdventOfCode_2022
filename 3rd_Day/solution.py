# part 1| *
import string

file = open('input.txt', 'r').read().split('\n')

st_contains = []
nd_contains = []

for lines in file:
    st_contains.append(lines[:int(len(lines)//2)])
    nd_contains.append(lines[int(len(lines)//2):])


def common_member(st_list, nd_list):
    result = [i for i in st_list if i in nd_list]
    return result


summary = []

for lines in file:
    member = common_member(lines[:int(len(lines)//2)], lines[int(len(lines)//2):])
    summary.append(member)

alphabet = list(string.ascii_letters)

score = []

for i in summary:
    points = int(alphabet.index(i[0]))+1
    score.append(points)

print(f'Sum of the priorities was: \033[32m{sum(score)}\033[0m \n')

# part 2| **
group = 3
groups = [file[n:n+group] for n in range(0, len(file), group)]


def three_common_member(st_list, nd_list, rd_list):
    result = [i for i in st_list if i in nd_list if i in rd_list]
    return result


summary = []

for i in groups:
    member = three_common_member(i[0], i[1], i[2])
    summary.append(member)

score = []

for i in summary:
    points = int(alphabet.index(i[0]))+1
    score.append(points)

print(f'Sum of the groupin badges was: \033[32m{sum(score)}\033[0m')

# part 1| *
file = open('input.txt', 'r').read().split('\n')

# stone - X - 1
# paper - Y - 2
# scissors - Z - 3
# win - 6
# draw - 3
# loss - 0

score = []
moves_score = []

for line in file:
    if line in ['A X', 'B Y', 'C Z']:  # draws
        score.append(3)
    elif line in ['A Y', 'B Z', 'C X']:  # wins
        score.append(6)
    elif line in ['A Z', 'B X', 'C Y']:  # losses
        score.append(0)
    else:
        continue

for line in file:
    if line[2] == 'X':  # stones
        moves_score.append(1)
    elif line[2] == 'Y':  # papers
        moves_score.append(2)
    elif line[2] == 'Z':  # scissors
        moves_score.append(3)
    else:
        continue

print(f'My first result was: \033[32m{sum(score)+sum(moves_score)}\033[0m \n')

# part 2| **
score = []
moves_score = []

for line in file:
    if line[2] == 'X':  # losses
        score.append(0)
    elif line[2] == 'Y':  # draws
        score.append(3)
    elif line[2] == 'Z':  # wins
        score.append(6)
    else:
        continue

for line in file:
    if line in ['C Z', 'A Y', 'B X']:  # stones
        moves_score.append(1)
    elif line in ['A Z', 'B Y', 'C X']:  # papers
        moves_score.append(2)
    elif line in ['B Z', 'C Y', 'A X']:  # scissors
        moves_score.append(3)
    else:
        continue

print(f'My second result was: \033[32m{sum(score)+sum(moves_score)}\033[0m')

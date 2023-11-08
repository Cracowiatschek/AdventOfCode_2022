# part 1| *
file = open('input.txt', 'r').read().split('\n')

head_x, head_y = 0, 0
tail_x, tail_y = 0, 0


def touching(x1, y1, x2, y2):
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1


def move(x, y):
    global head_x, head_y, tail_x, tail_y

    head_x += x
    head_y += y

    if not touching(head_x, head_y, tail_x, tail_y):
        sign_x = 0 if head_x == tail_x else (head_x - tail_x) / abs(head_x - tail_x)
        sign_y = 0 if head_y == tail_y else (head_y - tail_y) / abs(head_y - tail_y)

        tail_x += sign_x
        tail_y += sign_y


mapper = {
          "R": [1, 0],
          "U": [0, 1],
          "L": [-1, 0],
          "D": [0, -1]
        }

tail_positions = set()
tail_positions.add((tail_x, tail_y))

for line in file:
    direct, value = line.split(" ")
    value = int(value)
    x, y = mapper[direct]

    for n in range(value):
        move(x, y)
        tail_positions.add((tail_x, tail_y))

print(f'Positions of tail: \033[32m{len(tail_positions)}\033[0m')

# part 2| **
knots = [[0, 0] for i in range(10)]

head_x, head_y = 0, 0
tail_x, tail_y = 0, 0


def move(x, y):
    global knots
    knots[0][0] += x
    knots[0][1] += y

    for i in range(1, 10):
        head_x, head_y = knots[i - 1]
        tail_x, tail_y = knots[i]

        if not touching(head_x, head_y, tail_x, tail_y):
            sign_x = 0 if head_x == tail_x else (head_x - tail_x) / abs(head_x - tail_x)
            sign_y = 0 if head_y == tail_y else (head_y - tail_y) / abs(head_y - tail_y)

            tail_x += sign_x
            tail_y += sign_y

        knots[i] = [tail_x, tail_y]


tail_positions = set()
tail_positions.add((tail_x, tail_y))

for line in file:
    direct, value = line.split(" ")
    value = int(value)
    x, y = mapper[direct]

    for n in range(value):
        move(x, y)
        tail_positions.add(tuple(knots[-1]))

print(f'Knots: \033[32m{len(tail_positions)}\033[0m')

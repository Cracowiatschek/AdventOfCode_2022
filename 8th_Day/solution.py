# part 1| *
import numpy as np

file = open('input.txt', 'r').read().strip().split()

grid = [list(map(int, list(line))) for line in file]

n = len(grid)
m = len(grid[0])
grid = np.array(grid)

result = 0

for i in range(n):
    for j in range(m):
        h = grid[i, j]

        if j == 0 or np.amax(grid[i, :j]) < h:
            result += 1
        elif j == m - 1 or np.amax(grid[i, (j+1):]) < h:
            result += 1
        elif i == 0 or np.amax(grid[:i, j]) < h:
            result += 1
        elif i == n - 1 or np.amax(grid[(i+1):, j]) < h:
            result += 1

print(f'Visible trees are: \033[32m{result}\033[0m')
# part 2| **
corners = [[0, 1], [0, -1], [1, 0], [-1, 0]]

result = 0
for i in range(n):
    for j in range(m):
        h = grid[i, j]
        score = 1

        # Scan in 4 directions
        for di, dj in corners:
            ii, jj = i + di, j + dj
            dist = 0

            while (0 <= ii < n and 0 <= jj < m) and grid[ii, jj] < h:
                dist += 1
                ii += di
                jj += dj

                if (0 <= ii < n and 0 <= jj < m) and grid[ii, jj] >= h:
                    dist += 1

            score *= dist

        result = max(result, score)

print(f'Max score: \033[32m{result}\033[0m')

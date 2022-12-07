# Part One
with open("7thDay.txt") as file:
    lines = [x.strip().split() for x in file]

root = {".type": "d"}
cwd = None
path = []

for t in lines:
    if t[0] == "$":
        if t[1] == "cd":
            if t[2] == "/":
                cwd = root
            elif t[2] == "..":
                cwd = path.pop()
            else:
                path.append(cwd); cwd = cwd[t[2]]
    elif t[0] == "dir":
        cwd[t[1]] = {".type": "d"}
    else:
        cwd[t[1]] = {".type": "f", ".size": int(t[0])}

def getSize(n):
    if n[".type"] == "f": return n[".size"]
    return sum(getSize(v) for k, v in n.items() if not k.startswith("."))

def createSizeList(cwd, allSizes):
    allSizes.append(getSize(cwd))
    for k, v in cwd.items():
        if not k.startswith(".") and v[".type"] == "d":
            createSizeList(v, allSizes)

allSizes = []
createSizeList(root, allSizes)
print("Part One: " + str(sum(s for s in allSizes if s < 100_000)))

# Part Two
sizeFree = 70_000_000 - allSizes[0]
for d in sorted(allSizes):
    if sizeFree + d >= 30_000_000:
        print("Part Two: " + str (d))
        break

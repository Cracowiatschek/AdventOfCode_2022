#Part One

with open("7thDay.txt", "r") as file:
    lines = file.read().split("\n")

print(lines)

id = 0
allDir = []
commands = []
files = []

for i in lines:

    if i[0] == '$':
        commands.append([i[2:4],id])
    elif i[:3] == 'dir':
        allDir.append([i[4:],id])
    else:
        files.append([i.split(' '), id])

    id += 1

# catalogs = []
#
# for i in commands:
#     if i == 'cd' and lines[i[1]] != 'cd ..':
#         catalogs.append(lines[i[1]])
#     else:
#         pass
#


# def directories(commandList):
#
#     id = 0
#     allDir = []
#     commands = []
#     files = []
#
#     for i in commandList:
#         if i[0] == '$':
#             commands.append([i[2:4], id])
#         elif i[:3] == 'dir':
#             allDir.append([i[4:], id])
#         else:
#             files.append([i.split(' '), id])
#         id += 1
#
#     for dirs in allDir:
#         if


print(allDir)
print(commands)
print(files)
print(catalogs)
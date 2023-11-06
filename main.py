# Part 1

with open("8thDay.txt", "r") as file:
    lines = file.read().split("\n")

hor = []
ver = []


for i in lines:
    ln = []
    for n in i:
        ln.append(int(n))
    hor.append(ln)

x = 0

for i in range(len(lines)):
    ln = []
    y = 0

    for n in range(len(lines)):
        ln.append(int(lines[y][x]))
        y += 1

    ver.append(ln)
    x += 1



print(hor)
print(ver)

horizontal = []
horizontalReverse = []

for i in lines:
    data = list(i)
    h = []
    hR = []
    for n in data:
        h.append(int(n))
    data.reverse()
    for n in data:
        hR.append(int(n))
    horizontal.append(h)
    horizontalReverse.append(hR)


id = 0
vertical = []
verticalReverse = []


for i in range(len(lines)):
    v = []
    vR = []
    line = 0
    lineR = 98
    for n in range(len(lines)):
        v.append(int(lines[line][id]))
        vR.append(int(lines[lineR][id]))
        line += 1
        lineR -= 1
    vertical.append(v)
    verticalReverse.append(vR)
    id += 1

y = 0

def cords(list, result, orient):
    if orient == True
        y = 0
        x = 0
        xR = 98
        result = []
        for line in list:
            minimum = line[0]
            minimumR = line[-1]
            maximum = max(line)
            while minimum != maximum:
                for elements in line:
                    result.append([elements,x,y])
                    x += 1
                    minimum += 1
            while minimumR != maximum:
                for elements in line:
                    result.append([elements,xR,y])
                    xR += 1
                    minimumR += 1
            y += 1
    elif orinet == False:
        x = 0
        y = 0
        yR = 98
        result = []
        for lines in horizontal:
            minimum = lines[0]
            minimumR = lines[-1]
            maximum = max(lines)
            while minimum != maximum:
                for elements in lines:
                    result.append([elements, x, y])
                    x += 1
                    minimum += 1
            while minimumR != maximum:
                for elements in lines:
                    result.append([elements, xR, y])
                    xR += 1
                    minimumR += 1
    return result

for i in range(len(horizontal)):
    x = 0
    xR = 98
    cords = []
    mn = horizontal[y][0]
    mnR = horizontalReverse[y][0]
    mx = max(horizontal[y])
    while mn != mx:
        for n in horizontal[y]:
            if n == mn:
                cords.append([n, x, y])
                x += 1
                break
            else:
                x += 1
        mn += 1

    while mnR != mx:
        for n in horizontalReverse[y]:
            if n == mnR:
                cords.append([n, x, y])
                xR -= 1
                break
            else:
                xR -= 1
        mnR += 1

    # for i in cords:
    #     result.append(i)
    # y += 1

x = 0

for i in range(len(vertical)):
    y = 0
    yR = 98
    cords = []
    mn = vertical[x][0]
    mnR = verticalReverse[x][0]
    mx = max(vertical[x])
    while mn != mx:
        for n in vertical[x]:
            if n == mn:
                cords.append([n, x, y])
                y += 1
                break
            else:
                y += 1
        mn += 1

    while mnR != mx:
        for n in verticalReverse[x]:
            if n == mnR:
                cords.append([n, x, y])
                yR -= 1
                break
            else:
                yR -= 1
        mnR += 1

    # for i in cords:
    #     result.append(i)
    # x += 1

uniq = []

# for i in result:
#     if i[1:] not in uniq:
#        a = i[1:]
#        uniq.append(a)

print(len(uniq))
# for i in range(len(horizontal)):
#     id = 0
#     cordinates = []
#     idR = 98
#     minimum = horizontal[line][0]
#     minimumR = horizontalReverse[line][0]
#     maximum = max(horizontal[line])
#     while minimum != maximum and minimumR != maximum:
#         for n in horizontal[line]:
#             if n == minimumR:
#                 cordinates.append([n, id, line])
#                 id += 1
#                 break
#             else:
#                 id += 1
#         for n in horizontalReverse[lineR]:
#             if n == minimumR:
#                 cordinates.append([n, idR, lineR])
#                 idR -= 1
#                 break
#             else:
#                 idR -= 1
#         minimumR += 1
#
#     for n in cordinates:
#         result.append(n)
#
#     line += 1
#     lineR -= 1
#
# id = 0
# idR = 98
#
# for i in range(len(vertical)):
#     line = 0
#     cordinates = []
#     lineR = 98
#     minimum = vertical[id][0]
#     minimumR = verticalReverse[id][0]
#     maximum = max(vertical[id])
#     while minimum != maximum and minimumR != maximum:
#         for n in vertical[id]:
#             if n == minimumR:
#                 cordinates.append([n, id, line])
#                 line += 1
#                 break
#             else:
#                 line += 1
#         for n in verticalReverse[idR]:
#             if n == minimumR:
#                 cordinates.append([n, idR, lineR])
#                 lineR -= 1
#                 break
#             else:
#                 lineR -= 1
#         minimum += 1
#         minimumR += 1
#
#     for n in cordinates:
#         result.append(n)
#
#     id += 1
#     idR -= 1
#
# toprint = []
#
# for i in result:
#     toprint.append(i[1:])
#
# uniq = []
# [uniq.append(x) for x in toprint if x not in uniq]
# print(len(uniq))
# results = horizontalResult+horizontalReverseResult+verticalResult+verticalReverseResult
# uniq = []
# [uniq.append(x) for x in results if x not in uniq]
#
# print(len(uniq))

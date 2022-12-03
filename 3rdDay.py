# Part 1
import string


with open("3rdDay.txt", "r") as file:
    lines = file.read().split("\n")

stContains = []
ndContains = []

for i in lines:
    stContains.append(i[:int(len(i)//2)])
    ndContains.append(i[int(len(i)//2):])

def commonMember(stList, ndList):
    result = [i for i in stList if i in ndList]
    return result


result = []
for i in lines:
    member = commonMember(i[:int(len(i)//2)],i[int(len(i)//2):])
    result.append(member)


lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
alphabet = list(string.ascii_letters)

score = []

for i in result:
    points = alphabet.index(i[0])+1
    score.append(points)

print(sum(score))

# Part 2

N = 3
groups = [lines[n:n+N] for n in range(0, len(lines),N)]

def threeCommonMember(stList, ndList, rdList):
    result = [i for i in stList if i in ndList if i in rdList]
    return result

summary = []

for i in groups:
     member = threeCommonMember(i[0],i[1],i[2])
     summary.append(member)

ndScore = []

for i in summary:
    points = alphabet.index(i[0])+1
    ndScore.append(points)

print(sum(ndScore))

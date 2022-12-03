# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

with open("2ndDay.txt", "r") as file:
    lines = file.read().split("\n")

#print(lines)
#A - rock Y - paper
#B - paper X - scissors
#C - scissors Z - rock
#Rock = 1 Z  Win = 6
#Paper = 2 Y Draw = 3
#Scissors = 3 X  Loss = 0
listOfWins = ['A Y', 'B X', 'C Z']
listOfDraws = ['C X', 'A Z', 'B Y']
listOfLosses = ['A X', 'B Z', 'C Y']

result = []
def search(list, param, points):
    for i in range(len(list)):
        if list[i] == param:
            result.append(points)
        else:
            pass


def points(listOfWins, listOfDraws, listOfLosses):
    for i in lines:
        search(listOfWins,i,6)

    for i in lines:
        search(listOfDraws,i,3)

    for i in lines:
        search(listOfLosses,i,0)

    for i in lines:
        if i[2:] == 'X':
            result.append(3)
        elif i[2:] == 'Y':
            result.append(2)
        elif i[2:] == 'Z':
            result.append(1)

points(listOfWins,listOfDraws,listOfLosses)

print(result)
print('')
print(sum(result))
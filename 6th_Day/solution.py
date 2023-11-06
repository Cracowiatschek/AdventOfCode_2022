# part 1| *
file = list(open('input.txt', 'r').read())
marker_length = 4
result = []
start_position = 0


for i in range(len(file)-marker_length):
    section = file[start_position:start_position+marker_length]
    if len(list(set(section))) == marker_length:
        break
    elif len(list(set(section))) != marker_length:
        start_position += 1
        continue
    else:
        pass

end_position = start_position + marker_length

print(f'Chars need to processed before the first 4 marker: \033[32m{end_position}\033[0m \n')

# part 2| **
marker_length = 14
result = []
start_position = 0

for i in range(len(file)-marker_length):
    section = file[start_position:start_position+marker_length]
    if len(list(set(section))) == marker_length:
        break
    elif len(list(set(section))) != marker_length:
        start_position += 1
        continue
    else:
        pass

end_position = start_position + marker_length

print(f'Chars need to processed before the first 14 marker: \033[32m{end_position}\033[0m')

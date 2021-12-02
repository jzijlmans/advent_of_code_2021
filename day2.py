
def read_file(filename):
    with open(filename, 'r') as f:
        input = []
        for line in f:
            input.append(line)
    return input

filename = "C:/Users/jeroe/PycharmProjects/advent_of_code_2021/input_files/day2.txt"

input = read_file(filename)

depth = 0
pos = 0
for command in input:
    direction, num = command.split(" ")
    if direction == "forward":
        pos += int(num)
    elif direction == "up":
        depth -= int(num)
    elif direction == "down":
        depth += int(num)
    else:
        print("got unkown direction: " + direction)

print("assignment 1: " + str(depth * pos))

aim = 0
depth = 0
pos = 0
for command in input:
    direction, num = command.split(" ")
    if direction == "forward":
        pos += int(num)
        depth += aim * int(num)
    elif direction == "up":
        aim -= int(num)
    elif direction == "down":
        aim += int(num)
    else:
        print("got unkown direction: " + direction)
print("assignment 2: " + str(depth * pos))
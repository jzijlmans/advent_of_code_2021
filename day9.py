filename = "C:/Users/jeroe/PycharmProjects/advent_of_code_2021/input_files/day9.txt"

with open(filename) as f:
    grid = []

    for line in f:
        row = []
        for num in line[:-1]:
            row.append(int(num))
        grid.append(row)

score = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        next = []
        if not j == 0:
            next.append(grid[i][j-1])
        if not j == len(grid[i])-1:
            next.append(grid[i][j+1])
        if not i == 0:
           next.append(grid[i-1][j])
        if not i == len(grid)-1:
            next.append(grid[i+1][j])
        if grid[i][j] < min(next):
            score += grid[i][j] + 1
print('assignment1: ' + str(score))

def get_lowest_number(grid,i,j):
    if not j == 0:
        if grid[i][j - 1] < grid[i][j]:
            return get_lowest_number(grid, i, j-1)
    if not j == len(grid[i]) - 1:
        if grid[i][j + 1] < grid[i][j]:
            return get_lowest_number(grid, i, j+1)
    if not i == 0:
       if grid[i - 1][j] < grid[i][j]:
           return get_lowest_number(grid, i-1, j)
    if not i == len(grid) - 1:
        if grid[i + 1][j] < grid[i][j]:
            return get_lowest_number(grid, i+1, j)
    return i, j

lowest_numbers = {}
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] != 9:
            k, p = get_lowest_number(grid, i, j)
            id = k*len(grid[i])+p
            print(str(grid[i][j]) + " " + str(k) + " " + str(p))
            if not id in lowest_numbers:
                lowest_numbers[id] = 0
            lowest_numbers[id] += 1
basin_sizes = list(lowest_numbers.values())
basin_sizes.sort(reverse=True)
print(" Assignment 2: " + str(basin_sizes[0]*basin_sizes[1]*basin_sizes[2]))

# low=[]
# for i in range(len(input)):
#     lowest_top = True
#     lowest_bottom = True
#     lowest_right = True
#     lowest_left = True
#     if i-1 >= 0 and ((i % line_length) != 0):
#         if input[i] < input[i-1]:
#             lowest_left = True
#         else:
#             lowest_left = False
#     if (i+1 <= (len(input)-1)) and((i+1 % line_length)!=0):
#         if input[i] < input[i+1]:
#             lowest_right = True
#         else:
#             lowest_right = False
#     if i + line_length <= (len(input)-1):
#         if input[i] < input[i+line_length]:
#             lowest_bottom = True
#         else:
#             lowest_bottom = False
#     if i - line_length >= 0:
#         if input[i] < input[i-line_length]:
#             lowest_top = True
#         else:
#             lowest_top = False
#     if (lowest_top or lowest_top == None) and (lowest_right or lowest_right == None) and (lowest_bottom or lowest_bottom == None) and (lowest_left or lowest_left == None):
#         low.append(input[i])
#
# print(low)
# risk = [x+1 for x in low]
# print('assignment1: ' + str(sum(risk)))

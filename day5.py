filename = "C:/Users/jeroe/PycharmProjects/advent_of_code_2021/input_files/day5.txt"

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.diagonal = False
        if x1 == x2:
            self.line_points = [ [x1, y] for y in range(min(y1,y2),max(y2,y1)+1)]
        elif y1 == y2:
            self.line_points = [[x, y1] for x in range(min(x1,x2), max(x2,x1) + 1)]
        else:
            self.diagonal = True
            x_dir = 1 if x1 < x2 else -1
            y_dir = 1 if y1 < y2 else -1

            self.line_points = []
            for i in range(abs(x1-x2)+1):
                self.line_points.append([x1+x_dir*i,y1+y_dir*i])


def calculate_num_crosspoints(lines, y_max, x_max, count_diag):
    grid = []
    for i in range(y_max):
        grid.append([0] * x_max)

    for line in lines:
        if not line.diagonal or count_diag:
            for point in line.line_points:
                grid[point[0]][point[1]] += 1

    num_line_crosses = 0
    for i in range(x_max):
        for j in range(y_max):
            if grid[i][j] > 1:
                num_line_crosses += 1
    return num_line_crosses

def print_grid(grid):
    for i in grid:
        print(i)

lines = []
x_max = 0
y_max = 0
with open(filename) as f:
    for file_line in f:
        coords = file_line.rstrip().split(' -> ')
        x1, y1 = coords[0].split(',')
        x2, y2 = coords[1].split(',')
        x_max = int(x1) if x_max < int(x1) else x_max
        x_max = int(x2) if x_max < int(x2) else x_max
        y_max = int(y1) if y_max < int(y1) else y_max
        y_max = int(y2) if y_max < int(y2) else y_max
        lines.append(Line(int(x1),int(y1),int(x2),int(y2)))

x_max += 1
y_max += 1
num_line_crosses = calculate_num_crosspoints(lines, y_max, x_max, False)
print("assignment1: " + str(num_line_crosses))

num_line_crosses = calculate_num_crosspoints(lines, y_max, x_max, True)
print("assignment2: " + str(num_line_crosses))

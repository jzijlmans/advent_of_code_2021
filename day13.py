filename = "C:/Users/jeroe/PycharmProjects/advent_of_code_2021/input_files/day13.txt"

class Grid:
    def __init__(self, x_max, ymax):
        self.grid = []
        for y in range(ymax+1):
            self.grid.append([" "]*(x_max+1))

    def print(self):
        for y in self.grid:
            print(y)

    def add_point(self,x,y):
        self.grid[y][x] = "X"

    def fold(self, command ):
        if command[0] == 'y':
            for i in range(int(command[2:])+1, len(self.grid)):
                mirrored_y = int(command[2:]) - (i - int(command[2:]))
                for j in range(len(self.grid[i])):
                    if self.grid[i][j] == "X":
                        self.add_point(j,mirrored_y)

            self.grid = self.grid[0:int(command[2:])]
        elif command[0] == 'x':
            import pdb
            pdb.set_trace()
            for i in range(len(self.grid)):
                for j in range(int(command[2:])+1, len(self.grid[i])):
                    mirrored_x = int(command[2:]) - (j - int(command[2:]))
                    if self.grid[i][j] == "X":
                        self.add_point(mirrored_x,i)
                self.grid[i] = self.grid[i][0:int(command[2:])]

    def count_dots(self):
        num = 0
        for line in self.grid:
            for point in line:
                if point == 'X':
                    num+=1
        return num

folds=[]
points=[]
max_x=0
max_y=0
with open(filename) as f:
    for line in f:
        if line[:4] == "fold":
            folds.append(line[11:-1])
        elif line != "\n":
            x,y = line.rstrip().split(",")
            if int(x) > max_x:
                max_x = int(x)
            if int(y) > max_y:
                max_y = int(y)
            points.append([int(x),int(y)])

grid=Grid(max_x, max_y)
for point in points:
    grid.add_point(point[0],point[1])

# grid.print()
print("--------------------------")
for command in folds:
    grid.fold(command)
    print(" num of dots: " + str(grid.count_dots()))
    grid.print()

print(" num of dots: " + str(grid.count_dots()))


import math
filename = "C:/Users/jeroe/PycharmProjects/advent_of_code_2021/input_files/day15.txt"

class Grid():
    def __init__(self, grid):
        self.grid = grid
        self.values = {}
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                self.values[self.get_id([i,j])] = [i,j,100000]

    def get_id(self,point):
        return len(self.grid[0])*point[0]+point[1]

    def get_point(self,id):
        point_0 = math.floor(id/len(self.grid[0]))
        point_1 = id - point_0*len(self.grid[0])
        return [point_0,point_1]

    def get_neighbors(self,id):
        point = self.get_point(id)
        n = []
        if point[0]-1 > -1:
            n.append(self.get_id([point[0]-1, point[1]]))
        if point[0]+1 < len(self.grid):
            n.append(self.get_id([point[0]+1, point[1]]))
        if point[1]-1 > -1:
            n.append(self.get_id([point[0], point[1]-1]))
        if point[1]+1 < len(self.grid[point[0]]):
            n.append(self.get_id([point[0],point[1]+1]))
        return n

    def lowest_value_point(self,id_list):
        lowest_value = 100000000000
        lowest_point = None
        for id in id_list:
            if self.values[id][2] < lowest_value:
                lowest_value = self.values[id][2]
                lowest_point = id
        return lowest_point

    def print_values(self):
        for i in range(max(self.values.keys())+1):
            if (i % len(self.grid[0]) == 0):
                print('\n',end='')
            print(self.values[i][2],end='')
            print('  ',end='')

        print('\n')
        print('``````````````````````````````````````````````````````')

    def print_grid(self):
        for i in self.grid:
            print(i)

grid = []
g_2 = []
g_3 = []
g_4 =[]
g_5 =[]
with open(filename) as f:
    for line in f:
        l = []
        second = []
        third = []
        fourth = []
        fifth = []
        sixth = []
        seventh = []
        eight = []
        nineth = []
        for char in line.rstrip():
            l.append(int(char))
            char = int(char)
            if char+1 > 9:
                char = char-9
            second.append(int(char+1))
            if char+2 > 9:
                char = char-9
            third.append(int(char + 2))
            if char+3 > 9:
                char = char-9
            fourth.append(int(char + 3))
            if char+4 > 9:
                char = char-9
            fifth.append(int(char + 4))
            if char+5 > 9:
                char = char-9
            sixth.append(int(char + 5))
            if char+6 > 9:
                char = char-9
            seventh.append(int(char + 6))
            if char+7 > 9:
                char = char-9
            eight.append(int(char + 7))
            if char+8 > 9:
                char = char-9
            nineth.append(int(char + 8))
        grid.append(l+second+third+fourth+fifth)
        g_2.append(second+third+fourth+fifth+sixth)
        g_3.append(third+fourth+fifth+sixth + seventh)
        g_4.append(fourth+fifth+sixth + seventh + eight)
        g_5.append(fifth+sixth + seventh + eight + nineth)
    grid = grid + g_2 + g_3 + g_4 + g_5

g = Grid(grid)
#g.print_grid()
# g.print_values()
open_points = [g.get_id([len(grid)-1, len(grid[0])-1])]
g.values[g.get_id([len(grid)-1, len(grid[0])-1])][2] = g.grid[len(grid)-1][len(grid[0])-1]
# g.print_values()

found_start = False
while not found_start:
    point = g.lowest_value_point(open_points)
    open_points.remove(point)
    for n in g.get_neighbors(point):
        if n==0:
            found_start=True
        if g.values[n][2] == 100000:
            n_point = g.get_point(n)
            g.values[n][2] = g.values[point][2] + g.grid[n_point[0]][n_point[1]]
            open_points.append(n)

    # g.print_values()
#g.print_values()

print(g.values[0] + g.values[1] + g.values[500])

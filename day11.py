filename = "C:/Users/jeroe/PycharmProjects/advent_of_code_2021/input_files/day11.txt"

class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.flashes = 0

    def step(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j].up_energy(101):
                    self.flash(i,j)

    def flash(self, i, j):

        if j-1 >= 0:
            if self.grid[i][j-1].up_energy(self.grid[i][j].id):
                self.flash(i,j-1)
        if j+1 < len(self.grid[0]):
            if self.grid[i][j+1].up_energy(self.grid[i][j].id):
                self.flash(i,j+1)
        if i-1 >= 0:
            if self.grid[i-1][j].up_energy(self.grid[i][j].id):
                self.flash(i-1,j)
        if i+1 < len(self.grid):
            if self.grid[i+1][j].up_energy(self.grid[i][j].id):
                self.flash(i+1,j)
        if i - 1 >= 0 and j-1 >= 0:
            if self.grid[i-1][j-1].up_energy(self.grid[i][j].id):
                self.flash(i-1,j-1)
        if j-1 >= 0 and i+1 < len(self.grid):
            if self.grid[i+1][j-1].up_energy(self.grid[i][j].id):
                self.flash(i+1,j-1)
        if j + 1 < len(self.grid[0]) and i-1 >= 0:
            if self.grid[i-1][j+1].up_energy(self.grid[i][j].id):
                self.flash(i-1,j+1)
        if j + 1 < len(self.grid[0]) and i+1 < len(self.grid):
            if self.grid[i+1][j+1].up_energy(self.grid[i][j].id):
                self.flash(i+1,j+1)

    def end_day(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j].end_day():
                    self.flashes += 1

    def print(self):
        for i in range(len(self.grid)):
            linestr = ""
            for j in range(len(self.grid[i])):
                linestr += str(self.grid[i][j].energy) + " "
            print(linestr)

class octopus:
    def __init__(self, energy, id):
        self.energy = energy
        self.flashed = False
        self.gained_energy_from = []
        self.id = id

    def end_day(self):
        self.gained_energy_from = []
        if self.flashed:
            self.energy = 0
            self.flashed = False
            return True
        return False


    def up_energy(self, source):
        if source not in self.gained_energy_from:
            # print(str(self.id) + " : " + str(source))
            self.energy += 1
            self.gained_energy_from.append(source)
        return self.flash()

    def flash(self):
        if self.flashed == False:
            if self.energy > 9:
                self.flashed = True
                return True
        return False



with open(filename) as f:
    g = []
    id = 0
    for line in f:
        line.rstrip()
        row = []
        for char in line[:-1]:
            row.append(octopus(int(char), id))
            id += 1
        g.append(row)

    grid = Grid(g)
    grid.print()

    for i in range(100):
        last_total_flashes = grid.flashes
        grid.step()
        grid.end_day()
        # grid.print()


    print('assignment1: ' + str(grid.flashes))

    while not grid.flashes - last_total_flashes == 100:
        i += 1
        print("step: " + str(i+1))
        last_total_flashes = grid.flashes
        grid.step()
        grid.end_day()
        # grid.print()

    print('assignment2: ' + str(i+1))

filename = "C:/Users/jeroe/PycharmProjects/advent_of_code_2021/input_files/day7.txt"

def calc_fuel_1(positions, location):
    # import pdb
    # pdb.set_trace()
    return sum([abs(pos - location) for pos in positions])

def sum_till_N(N):
    return (N*(N + 1)) / 2

def calc_fuel_2(positions, location):

    return sum([sum_till_N(abs(pos - location)) for pos in positions])

with open(filename) as f:
    input = list(map(int, f.readline().rstrip().split(",")))

min_fuel_loc = max(input)
min_fuel = float("inf")
for i in range(min(input), max(input)):
    fuel = calc_fuel_1(input, i)
    if fuel < min_fuel:
        min_fuel = fuel
        min_fuel_loc = i

print('assignment1: fuel: ' + str(min_fuel) + ' location: ' + str(min_fuel_loc))

min_fuel_loc = max(input)
min_fuel = float("inf")
for i in range(min(input), max(input)):
    fuel = calc_fuel_2(input, i)
    if fuel < min_fuel:
        min_fuel = fuel
        min_fuel_loc = i

print('assignment2: fuel: ' + str(min_fuel) + ' location: ' + str(min_fuel_loc))
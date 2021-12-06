filename = "C:/Users/jeroe/PycharmProjects/advent_of_code_2021/input_files/day6.txt"

class Fish:
    def __init__(self, days_since_reproduce):
        self.days_since_reproduce = days_since_reproduce

    def new_day(self):
        self.days_since_reproduce -= 1
        if self.days_since_reproduce == -1:
            self.days_since_reproduce = 6
            return True
        else:
            return False

with open(filename) as f:
    input = f.readline().rstrip().split(",")

fish_pool = []
for num in input:
    fish_pool.append(Fish(int(num)))

for i in range(80):
    for fish in fish_pool:
        new_fish = fish.new_day()
        if new_fish:
            fish_pool.append(Fish(9))


print('Assignment 1: ' + str(len(fish_pool)))

num_fish_per_counter = [0,0,0,0,0,0,0,0,0]
for i in input:
    num_fish_per_counter[int(i)] += 1

for i in range(256):
    new_fish = num_fish_per_counter[0]

    for i in range(len(num_fish_per_counter)-1):
        if not i == 6:
            num_fish_per_counter[i] = num_fish_per_counter[i+1]
        else:
            num_fish_per_counter[i] = num_fish_per_counter[i+1] + new_fish

    num_fish_per_counter[8] = new_fish

print('assignment 2: ' + str(sum(num_fish_per_counter)))
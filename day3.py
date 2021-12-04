filename = "C:/Users/jeroe/PycharmProjects/advent_of_code_2021/input_files/day3.txt"

with open(filename, 'r') as f:
    diag_added_up=[0]*len(f.readline().rstrip())
    f.seek(0)
    num_lines=0
    for line in f:
        num_lines += 1
        i=0
        for char in line.rstrip():
            if char == "1":
                diag_added_up[i] += 1
            i+=1
gamma_str = ''
eps_str = ''
for num in diag_added_up:
    if num > (num_lines/2):
        gamma_str += '1'
        eps_str += '0'
    else:
        gamma_str += '0'
        eps_str += '1'

gamma = int(gamma_str,2)
eps = int(eps_str,2)
print('assignment 1 result: ' + str(gamma*eps))

## assignment 2:
def keep_candidates(candidates_list, num, pos):
    result = []
    for candidate in candidates_list:
        if candidate[pos] == str(num):
            result.append(candidate)
    return result

def filter(input, value_to_keep_on_1_most_common, value_to_keep_on_0_most_common ):
    candidates = input.copy()
    for i in range(len(candidates[0])):
        # determine most common digit:
        num = 0
        for can in candidates:
            num += int(can[i])
        if num >= (len(candidates) / 2):
            candidates = keep_candidates(candidates, value_to_keep_on_1_most_common, i)
        else:
            candidates = keep_candidates(candidates, value_to_keep_on_0_most_common, i)

        if len(candidates) == 1:
            return candidates[0]

with open(filename, 'r') as f:
    input = []
    for line in f:
        input.append(line.rstrip())



ox = int(filter(input,1,0),2)
co2 = int(filter(input,0,1),2)
print('assignment2: ' + str(ox * co2))
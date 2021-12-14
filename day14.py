filename = "C:/Users/jeroe/PycharmProjects/advent_of_code_2021/input_files/day14.txt"

with open(filename) as f:
    template = f.readline().rstrip()
    f.readline()
    rules = {}
    for line in f:
        part1 , part2 = line.rstrip().split(" -> ")
        rules[part1]=part2

string = template
for i in range(10):
    print(i)
    new_string = string[0]
    for j in range(0,len(string)-1):
        if string[j]+string[j+1] in rules:
            new_string = new_string + rules[string[j]+string[j+1]] +string[j+1]
        else:
            new_string = new_string + string[j+1]

    string = new_string

letter_counts = {}
for char in string:
    if char in letter_counts:
        letter_counts[char] +=1
    else:
        letter_counts[char] = 1

max_num = 0
min_num = 100000000000000
for key in letter_counts:
    if letter_counts[key] > max_num:
        max_num = letter_counts[key]
    if letter_counts[key] < min_num:
        min_num = letter_counts[key]
print(letter_counts)
print('assignment1: ' + str(max_num-min_num))

def add_to_dict(dict,pair, num):
    if pair in dict:
        dict[pair] += num
    else:
        dict[pair] = num

letter_pairs = {}
letter_nums = {}
for i in range(len(template)-1):
    add_to_dict(letter_pairs, template[i:i+2], 1)
    add_to_dict(letter_nums,template[i],1)
add_to_dict(letter_nums,template[-1], 1)

for i in range(40):
    next_letter_pairs = {}
    for letter_pair in letter_pairs:
        if letter_pair in rules:
            add_to_dict(next_letter_pairs, letter_pair[0]+rules[letter_pair], letter_pairs[letter_pair])
            add_to_dict(next_letter_pairs, rules[letter_pair]+letter_pair[1], letter_pairs[letter_pair])
            add_to_dict(letter_nums,rules[letter_pair],letter_pairs[letter_pair])
    letter_pairs = next_letter_pairs

    print(letter_pairs)
    print("!!!!!!!!")

max_num = 0
min_num = 1000000000000000000000
for pair in letter_nums:
    if letter_nums[pair] > max_num:
        max_num = letter_nums[pair]
    if letter_nums[pair] < min_num:
        min_num = letter_nums[pair]

print('assignment2: ' + str(max_num-min_num))

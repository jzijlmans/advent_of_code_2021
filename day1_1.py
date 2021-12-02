
def num_deeper_dives(input):
    output = 0
    for i in range(len(input)-1):
        if input[i+1]>input[i]:
            output += 1
    return(output)

def read_file(filename):
    with open(filename, 'r') as f:
        input = []
        for line in f:
            input.append(float(line))
    return input

def create_sliding_window(input):
    output=[]
    for i in range(len(input)-2):
        output.append(sum(input[i:i+3]))
    return output

filename = "C:/Users/jeroe/PycharmProjects/advent_of_code_2021/input_files/day1_1.txt"

input=read_file(filename)
print("assignment1: " + str(num_deeper_dives(input)))

sliding_window = create_sliding_window(input)
print("assignment2: " + str(num_deeper_dives(create_sliding_window(input))))
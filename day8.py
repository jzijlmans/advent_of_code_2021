filename = "C:/Users/jeroe/PycharmProjects/advent_of_code_2021/input_files/day8.txt"

def same_chars(string1, string2):
    for char in string1:
        if not char in string2:
            return False
    for char in string2:
        if not char in string1:
            return False
    return True

def remove_chars(string, chars):
    for char in chars:
        string = string.replace(char, '')
    return string

def remove_all_other_chars(string, chars):
    for char in ['a','b','c','d','e','f','g']:
        if char not in chars:
            string = remove_chars(string,char)
    return string

with open(filename) as f:
    ass1 = 0
    output_numbers = []
    for line in f:
        sig_pat , out = line.rstrip().split('|')
        sigs = sig_pat.split(' ')[:-1]
        outputs = out.split(' ')[1:]
        for output in outputs:
            if len(output) in [2,3,4,7]:
                ass1 += 1

        all_inputs = sigs + outputs

        #  0
        # 1 2
        #  3
        # 4 5
        #  6

        nums = ['abcdefg']*7
        for input in all_inputs:
            if len(input) == 2:
                nums[0] = remove_chars(nums[0], input)
                nums[1] = remove_chars(nums[1],input)
                nums[2] = remove_all_other_chars(nums[2],input)
                nums[3] = remove_chars(nums[3],input)
                nums[4] = remove_chars(nums[4],input)
                nums[5] = remove_all_other_chars(nums[5],input)
                nums[6] = remove_chars(nums[6],input)
            if len(input) == 3:
                nums[0] = remove_all_other_chars(nums[0],input)
                nums[1] = remove_chars(nums[1], input)
                nums[2] = remove_all_other_chars(nums[2],input)
                nums[3] = remove_chars(nums[3], input)
                nums[4] = remove_chars(nums[4], input)
                nums[5] = remove_all_other_chars(nums[5],input)
                nums[6] = remove_chars(nums[6], input)
            if len(input) == 4:
                nums[0] = remove_chars(nums[0], input)
                nums[1] = remove_all_other_chars(nums[1],input)
                nums[2] = remove_all_other_chars(nums[2], input)
                nums[3] = remove_all_other_chars(nums[3], input)
                nums[4] = remove_chars(nums[4], input)
                nums[5] = remove_all_other_chars(nums[5],input)
                nums[6] = remove_chars(nums[6], input)
            if len(input) == 6:
                nums[0] = remove_all_other_chars(nums[0],input)
                nums[1] = remove_all_other_chars(nums[1], input)
                nums[5] = remove_all_other_chars(nums[5], input)
                nums[6] = remove_all_other_chars(nums[6], input)
        for string in nums:
            if len(string) == 1:
                for i in range(len(nums)):
                    if len(nums[i]) > 1:
                        nums[i] = remove_chars(nums[i],string)

        number = ''
        for i in range(len(outputs)):
            for j in range(len(outputs[i])):
                outputs[i] = outputs[i].replace(outputs[i][j], str(nums.index(outputs[i][j])))
            if same_chars('012456',outputs[i]):
                number += '0'
            elif same_chars('25',outputs[i]):
                number += '1'
            elif same_chars('02346',outputs[i]):
                number += '2'
            elif same_chars('02356',outputs[i]):
                number += '3'
            elif same_chars('1235',outputs[i]):
                number += '4'
            elif same_chars('01356',outputs[i]):
                number += '5'
            elif same_chars('013456',outputs[i]):
                number += '6'
            elif same_chars('025',outputs[i]):
                number += '7'
            elif same_chars('0123456',outputs[i]):
                number += '8'
            elif same_chars('012356',outputs[i]):
                number += '9'
            else:
                print('unkown number: ' + outputs[i])
        output_numbers.append(int(number))

    print(output_numbers)
    print("Assignment 1: " + str(ass1))
    print("Assignment 2: " + str(sum(output_numbers)))

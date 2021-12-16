filename = "C:/Users/jeroe/PycharmProjects/advent_of_code_2021/input_files/day16.txt"

def hex_to_bin(string):
    m = {'0': '0000',
        '1' : '0001',
        '2' : '0010',
        '3' : '0011',
        '4': '0100',
        '5' : '0101',
        '6' : '0110',
        '7' : '0111',
        '8' : '1000',
        '9' : '1001',
        'A' : '1010',
        'B' : '1011',
        'C' : '1100',
        'D' : '1101',
        'E' : '1110',
        'F' : '1111'}
    result=''
    for char in string:
        result = result + m[char]
    return result

def bin(string):
    return


def calc_num(sub_nums, id):
    if id == 0:
        return sum(sub_nums)
    elif id == 1:
        product = 1
        for num in sub_nums:
            product = product * num
        return product
    elif id == 2:
        return min(sub_nums)
    elif id == 3:
        return max(sub_nums)
    elif id == 5:
        return int(sub_nums[0]>sub_nums[1])
    elif id == 6:
        return int(sub_nums[0]<sub_nums[1])
    elif id == 7:
        return int(sub_nums[0] == sub_nums[1])
    else:
        print(" wrong id passed: " + str(id))
        return 0

def read_package(bin_str, total_versions):
    version=int(bin_str[0: 3],2)
    total_versions += version
    id=int(bin_str[3: 6],2)
    if id == 4:
        i=6
        finished = False
        bin_num = ''
        while not finished:
            if bin_str[i] == '0':
                finished = True
            i+=1
            bin_num = bin_num + bin_str[i:i+4]
            i+=4
        num = int(bin_num,2)
        print('v:' + str(version) + ' I:' + str(id) + ' LV: ' + str(num))
        return bin_str[i:], total_versions, num
    else:
        if bin_str[6] == '0':
            bit_length = int(bin_str[7:22],2)
            sub_packages = bin_str[22:22+bit_length]
            num_sub_packages = 0
            print('v:' + str(version) + ' I:' + str(id) + ' S')
            sub_nums = []
            while len(sub_packages) >0 and not sub_packages == None:
                num_sub_packages +=1
                sub_packages, total_versions, sub_num = read_package(sub_packages, total_versions)
                sub_nums.append(sub_num)
            print('v:' + str(version) + ' I:' + str(id) + ' S:  ' + str(num_sub_packages))
            num = calc_num(sub_nums, id)
            return bin_str[22+bit_length:], total_versions, num
        else:
            num_sub_packages = int(bin_str[7:18],2)
            sub_packages = bin_str[18:]
            print('v:' + str(version) + ' I:' + str(id) + ' S')
            sub_nums = []
            for k in range(num_sub_packages):
                sub_packages, total_versions, sub_num = read_package(sub_packages, total_versions)
                sub_nums.append(sub_num)
            num = calc_num(sub_nums, id)
            print('v:' + str(version) + ' I:' + str(id) + ' S:  ' + str(num_sub_packages))
            return sub_packages, total_versions, num

with open(filename) as f:
    line= f.readline().rstrip()

bin_str = hex_to_bin(line)
print(bin_str)
tmp, total_versions, num = read_package(bin_str, 0)
print('Assignment1: ' + str(total_versions))
print('Assingment2: ' + str(num))
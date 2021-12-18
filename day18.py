import math
import copy
filename = "C:/Users/jeroe/PycharmProjects/advent_of_code_2021/input_files/day18.txt"

class Pair():
    def __init__(self, first, second, depth):
        self.f = first
        self.s = second
        self.d = depth
        self.addup_left = 0
        self.addup_right = 0
        # if type(self.f) == Pair:
        #     self.f.up_depth()
        # if type(self.s) == Pair:
        #     self.s.up_depth()

    def up_depth(self):
        self.d += 1
        if type(self.f) == Pair:
            self.f.up_depth()
        if type(self.s) == Pair:
            self.s.up_depth()

    def add(self, pair):
        self.up_depth()
        pair.up_depth()
        return Pair(self,pair, 0)

    def check_explode(self):
        if self.d >= 4 and not (type(self.f) == Pair or type(self.s) == Pair) :
            return True, True
        has_exploded = False
        if type(self.f) == Pair:
            has_exploded, exploded = self.f.check_explode()
            if exploded:
                self.addup_left = self.f.f
                if type(self.s) == Pair:
                    self.s.add_left(self.f.s)
                else:
                    self.s += self.f.s
            elif self.f.addup_left > 0:
                self.addup_left = self.f.addup_left
                self.f.addup_left = 0
            elif self.f.addup_right > 0:
                if type(self.s) == Pair:
                    self.s.add_left(self.f.addup_right)
                    self.f.addup_right = 0
                else:
                    self.s += self.f.addup_right
                    self.f.addup_right = 0
            if exploded:
                self.f = 0
        if not has_exploded and type(self.s) == Pair:
            has_exploded, exploded = self.s.check_explode()
            if exploded:
                self.addup_right = self.s.s
                if type(self.f) == Pair:
                    self.f.add_right(self.s.f)
                else:
                    if type(self.s.f) == Pair:
                        self.s.print()
                        print('\n')
                        print(self.s.f)
                    self.f += self.s.f
            elif self.s.addup_right > 0:
                self.addup_right = self.s.addup_right
                self.s.addup_right = 0
            elif self.s.addup_left > 0:
                if type(self.f) == Pair:
                    self.f.add_right(self.s.addup_left)
                    self.s.addup_left = 0
                else:
                    self.f += self.s.addup_left
                    self.s.addup_left = 0
            if exploded:
                self.s = 0
        return has_exploded, False

    def check_split(self):
        has_splitted = False
        if type(self.f) == Pair:
            has_splitted = self.f.check_split()
        else:
            if self.f > 9:
                self.f = Pair(math.floor(self.f/2), math.ceil(self.f/2), self.d + 1)
                has_splitted = True
        if not has_splitted:
            if type(self.s) == Pair:
                has_splitted = self.s.check_split()
            else:
                if self.s > 9:
                    self.s = Pair(math.floor(self.s/2), math.ceil(self.s/2), self.d + 1)
                    has_splitted = True
        return has_splitted

    def add_left(self,num):
        if type(self.f) == Pair:
            self.f.add_left(num)
        else:
            self.f += num

    def add_right(self,num):
        if type(self.s) == Pair:
            self.s.add_right(num)
        else:
            self.s += num

    def create_string(self, string):
        string += '['
        if type(self.f) == Pair:
            string = self.f.create_string(string)
        else:
            string += str(self.f)
        string +=','
        if type(self.s) == Pair:
            string = self.s.create_string(string)
        else:
            string += str(self.s)
        string += ']'
        return string

    def print(self):
        print(self.create_string(''))

def add(pair1, pair2):
    pair1.up_depth()
    pair2.up_depth()
    p = Pair(pair1,pair2,0)
    # p.print()
    # print('\n')
    finished = False
    while not finished:
        has_exploded = True
        while has_exploded:
            has_exploded, exploded = p.check_explode()
            # if has_exploded:
                # p.print()
                # print('\n')
        has_splitted = p.check_split()
        # if has_splitted:
            # p.print()
            # print('\n')
        if not has_splitted:
            finished = True
    return p

def create_pair_from_string(string):
    depth = -1
    code = 'global result_pair; result_pair='
    for char in string:
        if char == '[':
            code += 'Pair('
            depth += 1
        elif char == ']':
            code += ', ' + str(depth) + ')'
            depth += -1
        elif char == ',':
            code += ','
        elif char == " " or char == '\n':
            continue
        else:
            code += char
    exec(code)
    global result_pair
    return result_pair

def calc_mag(pair):
    mag = 0
    if type(pair.f) == Pair:
        mag+= 3*calc_mag(pair.f)
    else:
        mag += 3*pair.f
    if type(pair.s) == Pair:
        mag += 2*calc_mag(pair.s)
    else:
        mag += 2*pair.s
    return mag

    return mag

# with open(filename) as f:
#     line1 = f.readline()
#     p = create_pair_from_string(line1)
#     p.print()
#     for line in f:
#         print('+')
#         p_to_add = create_pair_from_string(line)
#         p_to_add.print()
#         print('=')
#         p = add(p,p_to_add)
#         p.print()
#         p = create_pair_from_string(p.create_string(''))
#
# print(calc_mag(p))
ps = []
with open(filename) as f:
    for line in f:
        ps.append(create_pair_from_string(line))

# p = add(copy.deepcopy(ps[0]),copy.deepcopy(ps[1]))
# p.print()
# mag = calc_mag(p)
# print(mag)
# ps[0].print()

max_mag = 0
for i in range(len(ps)):
    for j in range(len(ps)):
        print(ps[i].create_string(''))
        mag = calc_mag(add(copy.deepcopy(ps[i]),copy.deepcopy(ps[j])))
        if mag > max_mag:
            max_mag = mag
        print( str(mag) + ' = ' + ps[i].create_string('') + ' + ' + ps[j].create_string(''))
print(max_mag)



# p1 = create_pair_from_string('[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]')
# p2 = create_pair_from_string('[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]')
# p = add(p1,p2)
# p.print()

# p1 = create_pair_from_string('[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]')
# p1.print()
# p2 = create_pair_from_string('[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]')
# print('+')
# p2.print()
# p3 = add(p1,p2)
# print('=')
# p3.print()
# print('+')
# p4 = create_pair_from_string('[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]')
# p4.print()
# print('=')
# p3 = create_pair_from_string(p3.create_string(''))
# p5 = add(p3,p4)
# p5.print()

# p3 = create_pair_from_string('[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]')
# p4 = add(p1,p2)
# p4 = create_pair_from_string(p4.create_string(''))
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# p5 = add(p4,p3)
# p5.print()

# add(Pair(Pair(Pair(Pair(4,3,3),4,2),4,1),Pair(7,Pair(Pair(8,4,3),9,2),1),0), Pair(1,1,0)) #[[[[4,3],4],4],[7,[[8,4],9]]] + [1,1]


# p = Pair(Pair(Pair(Pair(Pair(9,8,4),1,3),2,2), 3, 1), 4, 0) #[[[[[9,8],1],2],3],4]
# p = Pair(7, Pair(6, Pair(5, Pair(4, Pair(3,2,4),3),2),1),0) #[7,[6,[5,[4,[3,2]]]]]
# p = Pair(Pair(6,Pair(5,Pair(4,Pair(3,2,4),3),2),1),1,0)#[[6,[5,[4,[3,2]]]],1]
# p = Pair(Pair(3,Pair(2,Pair(1,Pair(7,3,4),3),2),1),Pair(6,Pair(5,Pair(4,Pair(3,2,4),3),2),1),0)#[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]

# p.print()
# print('\n')
# has_exploded = True
# while has_exploded:
#     has_exploded, exploded = p.check_explode()
#     p.print()
#     print('\n')

# p = Pair(15,15,0)
# p.print()
# print('\n')
# p.check_split()
# p.print()
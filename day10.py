filename = "C:/Users/jeroe/PycharmProjects/advent_of_code_2021/input_files/day10.txt"

score = 0
score2s = []
with open(filename) as f:
    for l in f:
        l.rstrip()

        expected_queue = []
        corrupted = False
        for char in l:
            if char == "\n":
                continue
            if char == "{":
                expected_queue.append("}")
            elif char == "[":
                expected_queue.append("]")
            elif char == "<":
                expected_queue.append(">")
            elif char == "(":
                expected_queue.append(")")
            elif char != expected_queue[-1]:
                corrupted=True
                if char == ")":
                    score += 3
                elif char == "]":
                    score += 57
                elif char == "}":
                    score += 1197
                elif char == ">":
                    score += 25137
                break
            else:
                expected_queue.pop(-1)
        if not corrupted:
            print(expected_queue)
            score2 = 0
            for char in reversed(expected_queue):
                score2 = score2*5
                if char ==")":
                    score2 += 1
                if char =="]":
                    score2 += 2
                if char =="}":
                    score2 += 3
                if char ==">":
                    score2 += 4
            score2s.append(score2)
print('assignment1: ' + str(score))
score2s.sort()
print('assignment2: ' + str(score2s[int(len(score2s)/2-0.5)]))
from collections import defaultdict
import statistics

def part_1(raw_data):
    scores = defaultdict()
    scores[')'] = 3
    scores[']'] = 57
    scores['}'] = 1197
    scores['>'] = 25137
    openers = set(['(', '[', '{', '<'])

    ans = 0

    for line in raw_data:
        stack = []
        for char in line:
            if char in openers:
                stack.append(char)
            elif char == ')' and stack.pop() != '(':
                ans += scores[')']
            elif char == ']' and stack.pop() != '[':
                ans += scores[']']
            elif char == '}' and stack.pop() != '{':
                ans += scores['}']
            elif char == '>' and stack.pop() != '<':
                ans += scores['>']

    return ans

def helper(line):
    # if the line isn't corrupt, return a value > 0
    openers = set(['(', '[', '{', '<'])
    stack = []
    ans = 0

    for char in line:
        if char in openers:
            stack.append(char)
        elif char == ')' and stack.pop() != '(':
            return 0
        elif char == ']' and stack.pop() != '[':
            return 0
        elif char == '}' and stack.pop() != '{':
            return 0
        elif char == '>' and stack.pop() != '<':
            return 0

    while stack:
        ans *= 5
        n = stack.pop()
        if n == '(':
            ans += 1
        elif n == '[':
            ans += 2
        elif n == '{':
            ans += 3
        elif n == '<':
            ans += 4

    return ans

def part_2(raw_data):
    ans = []

    for line in raw_data:
        line_val = helper(line)
        if line_val > 0:
            ans.append(line_val)

    return statistics.median(ans)

 
def file_reader(file_name):
    input_file = open(file_name, 'r')
    inputs_raw = input_file.readlines()
    for i in range(len(inputs_raw)):
        inputs_raw[i] = inputs_raw[i].replace('\n', '')
    return inputs_raw

print(part_1(file_reader('input_10.txt')))
print(part_2(file_reader('input_10.txt')))

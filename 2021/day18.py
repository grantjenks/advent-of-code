# Part 1
import json

lines = text.splitlines()
json_nums = list(map(json.loads, lines))

def json_to_parens(num):
    tokens = []
    def visit(num):
        if isinstance(num, int):
            tokens.append(num)
        else:
            tokens.append('(')
            for part in num:
                visit(part)
            tokens.append(')')
    visit(num)
    return tokens

def add(left, right):
    result = ['(', *left, *right, ')']
    result = simplify(result)
    return result

def simplify(paren):
    while True:
        nest = 0
        for index, item in enumerate(paren):
            if item == '(':
                nest += 1
                explode = (
                    nest > 4
                    and isinstance(paren[index + 1], int)
                    and isinstance(paren[index + 2], int)
                    and paren[index + 3] == ')'
                )
                if explode:
                    left = paren[index + 1]
                    right = paren[index + 2]
                    for prev in range(index - 1, -1, -1):
                        if isinstance(paren[prev], int):
                            paren[prev] += left
                            break
                    for next in range(index + 4, len(paren)):
                        if isinstance(paren[next], int):
                            paren[next] += right
                            break
                    paren[index:(index+4)] = [0]
                    break
            elif item == ')':
                nest -= 1
        else:
            for index, item in enumerate(paren):
                if isinstance(item, int) and item >= 10:
                    split = ['(', item // 2, (item + 1) // 2, ')']
                    paren[index:(index + 1)] = split
                    break
            else:
                break
    return paren

parens = list(map(json_to_parens, json_nums))
result = parens[0]
for paren in parens[1:]:
    result = add(result, paren)

def magnitude(paren):
    stack = []
    for value in paren:
        if isinstance(value, int):
            stack.append(value)
        elif value == ')':
            right = stack.pop()
            left = stack.pop()
            total = 3 * left + 2 * right
            stack.append(total)
    return stack[0]

print(magnitude(result))

# Part 2
from itertools import permutations

totals = []
for left, right in permutations(parens, 2):
    left = list(left)
    right = list(right)
    total = magnitude(add(left, right))
    totals.append(total)

print(max(totals))

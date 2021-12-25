# Part 1
from collections import namedtuple
from functools import lru_cache
from operator import add, mul, floordiv, mod, eq

lines = text.splitlines()
instrs = [line.split() for line in lines]
regs = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
index = 0
bin_ops = {'add': add, 'mul': mul, 'div': floordiv, 'mod': mod, 'eql': eq}

Var = namedtuple('Var', 'index')


@lru_cache(maxsize=None)
def limits(node):
    if isinstance(node, int):
        return (node, node)
    if isinstance(node, Var):
        return (1, 9)
    if isinstance(node, tuple):
        op, left, right = node
        left_lo, left_hi = limits(left)
        right_lo, right_hi = limits(right)

        if op == add:
            return left_lo + right_lo, left_hi + right_hi
        if op == mul:
            return left_lo * right_lo, left_hi * right_hi
        if op == floordiv:
            return left_lo // right_hi, left_hi // right_lo
        if op == mod:
            return 0, right_hi
        if op == eq:
            return 0, 1

    return float('-inf'), float('inf')


def optimize(node):
    if isinstance(node, tuple):
        op, left, right = node

        if isinstance(left, int) and isinstance(right, int):
            return int(op(left, right))
        if op == mul and (left == 0 or right == 0):
            return 0
        if op == mul and left == 1:
            return right
        if op == mul and right == 1:
            return left
        if op == add and left == 0:
            return right
        if op == add and right == 0:
            return left
        if op == floordiv and left == 0:
            return 0
        if op == floordiv and right == 1:
            return left
        if op == eq:
            if isinstance(left, int) and isinstance(right, Var) and left >= 10:
                return 0
            left_lo, left_hi = limits(left)
            right_lo, right_hi = limits(right)
            if left_hi < right_lo or right_hi < left_lo:
                return 0
        if op == mul and isinstance(left, tuple) and isinstance(right, int):
            if left[0] == add:
                left = (mul, left[1], right)
                left = optimize(left)
                right = (mul, left[2], right)
                right = optimize(right)
                node = add, left, right
                node = optimize(node)
                return node
            if left[0] == mul and isinstance(left[2], int):
                return mul, left[1], left[2] * right
        if op in (add, mul) and isinstance(left, tuple) and isinstance(right, int):
            if left[0] == op and isinstance(left[2], int):
                return op, left[1], op(left[2], right)
        if op in (add, mul) and isinstance(right, tuple) and isinstance(left, int):
            node = op, right, left
            node = optimize(node)
            return node
        if op in (add, mul) and isinstance(left, tuple) and isinstance(right, tuple):
            if left[0] == op and isinstance(left[2], int):
                if right[0] == op and isinstance(right[2], int):
                    subnode = op, left[1], right[1]
                    subnode = optimize(subnode)
                    node = op, subnode, op(left[2], right[2])
                    node = optimize(node)
                    return node

    return node


for instr in instrs:
    op, reg, *other = instr
    expr = regs[reg]

    if op in bin_ops:
        other, = other
        if other.islower():
            expr2 = regs[other]
        else:
            expr2 = int(other)
        node = (bin_ops[op], expr, expr2)
        node = optimize(node)
        regs[reg] = node
    else:
        assert op == 'inp'
        regs[reg] = Var(index)
        index += 1

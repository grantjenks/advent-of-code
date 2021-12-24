# Part 1

text = """
#############
#...........#
###C#C#B#D###
  #D#A#B#A#
  #########
"""

spaces = """
#############
#abcdefghijk#
###l#n#p#r###
  #m#o#q#s#
  #########
"""

grid = {}
for pod, space in zip(text, spaces):
    if space.islower():
        grid[space] = pod

paths = {
    'a': {
        'l': 'bcl',
        'm': 'bclm',
        'n': 'bcden',
        'o': 'bcdeno',
        'p': 'bcdefgp',
        'q': 'bcdefgpq',
        'r': 'bcdefghir',
        's': 'bcdefghirs',
    },
    'b': {
        'l': 'cl',
        'm': 'clm',
        'n': 'cden',
        'o': 'cdeno',
        'p': 'cdefgp',
        'q': 'cdefgpq',
        'r': 'cdefghir',
        's': 'cdefghirs',
    },
    'd': {
        'l': 'cl',
        'm': 'clm',
        'n': 'en',
        'o': 'eno',
        'p': 'efgp',
        'q': 'efgpq',
        'r': 'efghir',
        's': 'efghirs',
    },
    'f': {
        'l': 'edcl',
        'm': 'edclm',
        'n': 'en',
        'o': 'eno',
        'p': 'gp',
        'q': 'gpq',
        'r': 'ghir',
        's': 'ghirs',
    },
    'h': {
        'l': 'gfedcl',
        'm': 'gfedclm',
        'n': 'gfen',
        'o': 'gfeno',
        'p': 'gp',
        'q': 'gpq',
        'r': 'ir',
        's': 'irs',
    },
    'j': {
        'l': 'ihgfedcl',
        'm': 'ihgfedclm',
        'n': 'ihgfen',
        'o': 'ihgfeno',
        'p': 'ihgp',
        'q': 'ihgpq',
        'r': 'ir',
        's': 'irs',
    },
    'k': {
        'l': 'jihgfedcl',
        'm': 'jihgfedclm',
        'n': 'jihgfen',
        'o': 'jihgfeno',
        'p': 'jihgp',
        'q': 'jihgpq',
        'r': 'jir',
        's': 'jirs',
    },
    'l': {
        'a': 'cba',
        'b': 'cb',
        'd': 'cd',
        'f': 'cdef',
        'h': 'cdefgh',
        'j': 'cdefghij',
        'k': 'cdefghijk',
    },
    'm': {
        'a': 'lcba',
        'b': 'lcb',
        'd': 'lcd',
        'f': 'lcdef',
        'h': 'lcdefgh',
        'j': 'lcdefghij',
        'k': 'lcdefghijk',
    },
    'n': {
        'a': 'edcba',
        'b': 'edcb',
        'd': 'ed',
        'f': 'ef',
        'h': 'efgh',
        'j': 'efghij',
        'k': 'efghijk',
    },
    'o': {
        'a': 'nedcba',
        'b': 'nedcb',
        'd': 'ned',
        'f': 'nef',
        'h': 'nefgh',
        'j': 'nefghij',
        'k': 'nefghijk',
    },
    'p': {
        'a': 'gfedcba',
        'b': 'gfedcb',
        'd': 'gfed',
        'f': 'gf',
        'h': 'gh',
        'j': 'ghij',
        'k': 'ghijk',
    },
    'q': {
        'a': 'pgfedcba',
        'b': 'pgfedcb',
        'd': 'pgfed',
        'f': 'pgf',
        'h': 'pgh',
        'j': 'pghij',
        'k': 'pghijk',
    },
    'r': {
        'a': 'ihgfedcba',
        'b': 'ihgfedcb',
        'd': 'ihgfed',
        'f': 'ihgf',
        'h': 'ih',
        'j': 'ij',
        'k': 'ijk',
    },
    's': {
        'a': 'rihgfedcba',
        'b': 'rihgfedcb',
        'd': 'rihgfed',
        'f': 'rihgf',
        'h': 'rih',
        'j': 'rij',
        'k': 'rijk',
    },
}

constraints = {
    'l': ('m', 'A'),
    'n': ('o', 'B'),
    'p': ('q', 'C'),
    'r': ('s', 'D'),
}

energy = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

ideal = dict(zip('lmnopqrs', 'AABBCCDD'))

def goal(grid):
    return all(grid[space] == pod for space, pod in ideal.items())

best = float('inf')

def organize(cost):
    global best

    if goal(grid):
        if cost < best:
            best = cost
            print('Best', best)
        return

    if cost >= best:
        return

    for space, pod in grid.items():
        if not pod.isupper():
            continue  # Not a pod.

        if space in ideal and ideal[space] == pod:
            if space in constraints:
                constraint_space, constraint_pod = constraints[space]
                if grid[constraint_space] == constraint_pod:
                    continue  # Pod is already in the correct space.
            else:
                continue  # Pod is already in the correct space.

        for target, path in paths[space].items():
            if not all(grid[path_space] == '.' for path_space in path):
                continue  # Path is not clear.

            simulate = False

            if target in ideal:
                if ideal[target] != pod:
                    continue  # Not the right room for this pod.

                if target in constraints:
                    constraint_space, constraint_pod = constraints[target]
                    if grid[constraint_space] == constraint_pod:
                        simulate = True
                else:
                    simulate = True
            else:
                simulate = True

            if simulate:
                grid[space] = '.'
                grid[target] = pod
                organize(cost + len(path) * energy[pod])
                grid[space] = pod
                grid[target] = '.'

# organize(0)

print(best)

# Part 2 (copied)

text = """
#############
#...........#
###C#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #D#A#B#A#
  #########
"""

from collections import Counter
from copy import deepcopy

#############
#...........#
###C#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #D#A#B#A#
  #########
A = ['C', 'D', 'D', 'D']
B = ['C', 'C', 'B', 'A']
C = ['B', 'B', 'A', 'B']
D = ['D' ,'A', 'C', 'A']

TOP = []
while len(TOP) < 11:
  TOP.append('E')
start = ({'A': A, 'B': B, 'C': C, 'D': D}, TOP)

COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
def done(state):
  bot, top = state
  for k,v in bot.items():
    for vv in v:
      if vv!=k:
        return False
  return True

def can_move_from(k, col):
  for c in col:
    if c!=k and c!='E':
      return True
  return False

def can_move_to(k,col):
  for c in col:
    if c!=k and c!='E':
      return False
  return True

def bot_idx(bot):
  return {'A': 2, 'B': 4, 'C': 6, 'D': 8}[bot]

def top_idx(col):
  for i,c in enumerate(col):
    if c!='E':
      return i
  return None

def dest_idx(col):
  for i,c in reversed(list(enumerate(col))):
    if c=='E':
      return i
  return None

def between(a, bot, top):
  # 0 1 A 3 B 5 C 7 D 9 10
  return (bot_idx(bot)<a<top) or (top<a<bot_idx(bot))
assert between(1, 'A', 0)

def clear_path(bot, top_idx, top):
  for ti in range(len(top)):
    if between(ti, bot, top_idx) and top[ti]!='E':
      return False
  return True

def show(state):
  bot, top = state
  C = Counter()
  for c in top:
    C[c] += 1
  for k,v in bot.items():
    for c in v:
      C[c] += 1
  assert C['A'] == 4
  assert C['B'] == 4
  assert C['C'] == 4
  assert C['D'] == 4
  assert C['E'] == 11
  assert top[2] == 'E'
  assert top[4] == 'E'
  assert top[6] == 'E'
  assert top[8] == 'E'

DP = {}
def f(state):
  # given a state, what is the cost to get to "done"?
  show(state)
  # move top -> L or R
  # move L or R -> 
  # always move to destination ASAP
  bot, top = state
  key = (tuple((k, tuple(v)) for k,v in bot.items()), tuple(top))
  if done(state):
    return 0
  if key in DP:
    return DP[key]
  # move to dest if possible
  for i,c in enumerate(top):
    if c in bot and can_move_to(c,bot[c]):
      if clear_path(c, i, top):
        di = dest_idx(bot[c])
        assert di is not None
        dist = di + 1 + abs(bot_idx(c)-i)
        cost = COST[c] * dist
        new_top = list(top)
        new_top[i] = 'E'
        top[i] = 'E'
        new_bot = deepcopy(bot)
        new_bot[c][di] = c
        #print(f'Moved top={i} c={c} dest={di}')
        return cost + f((new_bot, new_top))

  ans = int(1e9)
  for k,col in bot.items():
    if not can_move_from(k, col):
      continue
    ki = top_idx(col)
    if ki is None:
      continue
    c = col[ki]
    for to_ in range(len(top)):
      if to_ in [2, 4, 6, 8]:
        continue
      if top[to_] != 'E':
        continue
      if clear_path(k, to_, top):
        dist = ki + 1 + abs(to_ - bot_idx(k))
        new_top = list(top)
        assert new_top[to_] == 'E'
        new_top[to_] = c
        new_bot = deepcopy(bot)
        assert new_bot[k][ki] == c
        new_bot[k][ki] = 'E'
        #print(f'Moved col={k} idx={ki} c={c} to {to_}')
        ans = min(ans, COST[c]*dist + f((new_bot, new_top)))
  DP[key] = ans
  #print(len(DP), ans)
  return ans

print(f(start))

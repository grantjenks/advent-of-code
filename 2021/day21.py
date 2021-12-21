# Part 1
from itertools import count, cycle

players = {
    # player: (space, score)
    'Player 1': (4, 0),
    'Player 2': (1, 0),
}

rolls = ((i % 100) + 1 for i in count())

for turns, player in enumerate(cycle(players.keys()), start=1):
    dice = (next(rolls), next(rolls), next(rolls))
    moves = sum(dice)
    space, score = players[player]
    space = (space - 1 + moves) % 10 + 1
    score += space
    players[player] = (space, score)
    if score >= 1_000:
        break

print(turns * 3 * min(score for _, score in players.values()))

# Part 2
from functools import lru_cache
from itertools import product

scenarios = Counter(sum(dice) for dice in product(*([range(1, 4)] * 3)))

@lru_cache(maxsize=None)
def play(p1_space, p1_score, p2_space, p2_score, p1_turn):
    p1_wins_total = p2_wins_total = 0
    for moves, count in scenarios.items():
        if p1_turn:
            p1_space_next = (p1_space - 1 + moves) % 10 + 1
            p1_score_next = p1_score + p1_space_next
            if p1_score_next >= 21:
                p1_wins, p2_wins = 1, 0
            else:
                p1_wins, p2_wins = play(
                    p1_space_next, p1_score_next, p2_space, p2_score, False
                )
        else:
            p2_space_next = (p2_space - 1 + moves) % 10 + 1
            p2_score_next = p2_score + p2_space_next
            if p2_score_next >= 21:
                p1_wins, p2_wins = 0, 1
            else:
                p1_wins, p2_wins = play(
                    p1_space, p1_score, p2_space_next, p2_score_next, True
                )
        p1_wins_total += count * p1_wins
        p2_wins_total += count * p2_wins
    return p1_wins_total, p2_wins_total

print(max(play(4, 0, 1, 0, True)))

# Part 1
lines = text.splitlines()
boards = [dict() for _ in range(100)]
for index in range(5):
    for board, row in enumerate(lines[2+index::6]):
        for col, value in enumerate(map(int, row.split())):
            boards[board][index, col] = value
all_marks = [set() for _ in range(len(boards))]
def bingo(marks):
    return (
        any(all((i, j) in marks for i in range(5)) for j in range(5))
        or any(all((j, i) in marks for i in range(5)) for j in range(5))
    )
boards = [{value: key for key, value in board.items()} for board in boards]
for num in nums:
    for index, board in enumerate(boards):
        if num in board:
            all_marks[index].add(board[num])
    if any(bingo(marks) for marks in all_marks):
        print('bingo!')
        break
next(index for index, marks in enumerate(all_marks) if bingo(marks))
sum(num for num, pair in boards[81].items() if pair not in all_marks[81])
num
14 * 603

# Part 2
boards = [dict() for _ in range(100)]
for index in range(5):
    for board, row in enumerate(lines[2+index::6]):
        for col, value in enumerate(map(int, row.split())):
            boards[board][index, col] = value
boards = [{value: key for key, value in board.items()} for board in boards]
all_marks = [set() for _ in range(len(boards))]
for num in nums:
    for index, board in enumerate(boards):
        if num in board:
            all_marks[index].add(board[num])
    winners = [index for index, marks in enumerate(all_marks) if bingo(marks)]
    winners.sort(reverse=True)
    for winner in winners:
        board = boards.pop(winner)
        marks = all_marks.pop(winner)
    if not boards:
        print('Done!')
        break
sum(num for num, pair in board.items() if pair not in marks) * num

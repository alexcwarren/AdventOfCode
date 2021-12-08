def parse(lines):
    data = None
    with open(filename, 'r') as infile:
        data = infile.read()
    lines = data.split('\n')

    numbers_called = [int(n) for n in lines[0].split(',')]

    board_lines = lines[2:]
    boards = list()
    board = list()
    for i,line in enumerate(board_lines):
        if line != '':
            board.append([int(n) for n in line.split()])
        if line == '' or i >= len(board_lines) - 1:
            boards.append(board)
            board = list()
    
    return (numbers_called, boards)


def part_one(numbers_called, boards):
    print(f'Running Part 1:')

    winning_sum = 0
    last_number = 0
    is_won = False
    WIN_COUNT = len(boards[0])
    
    board_sums = [0 for __ in boards]
    board_row_counts = [[0 for __ in board] for board in boards]
    board_col_counts = [[0 for __ in board] for board in boards]

    for n,num_called in enumerate(numbers_called):
        for b,board in enumerate(boards):
            board_is_marked = False
            for r,row in enumerate(board):
                for c,num in enumerate(row):
                    if n == 0:
                        board_sums[b] += num
                    if num == num_called:
                        board_sums[b] -= num
                        board_row_counts[b][r] += 1
                        board_col_counts[b][c] += 1
                        board_is_marked = True
                        break
                if board_is_marked:
                    break
            
            # Check for winner
            if WIN_COUNT in board_row_counts[b] or WIN_COUNT in board_col_counts:
                winning_sum = board_sums[b]
                last_number = num_called
                is_won = True
                break
        
        if is_won:
            break

    score = winning_sum * last_number

    # When using 'sample.in' data:
    # if winning_sum == 188 and last_number == 24 and score == 4512:
    #     print('SUCCESS')
    # else:
    #     print('FAILURE')
    
    print(f'    Sum = {winning_sum}, Last number called = {last_number}')
    print(f'    ==> Score = {score}\n')


def part_two(numbers_called, boards):
    print(f'Running Part 2:')
    
    winning_sum = 0
    last_number = 0
    WIN_COUNT = len(boards[0])
    
    board_sums = [sum([sum(row) for row in board]) for board in boards]
    board_row_counts = [[0 for __ in board] for board in boards]
    board_col_counts = [[0 for __ in board] for board in boards]
    won_boards = list()

    for n,num_called in enumerate(numbers_called):
        for b,board in enumerate(boards):
            if b in won_boards:
                continue
            board_is_marked = False
            for r,row in enumerate(board):
                for c,num in enumerate(row):
                    if num == num_called:
                        board_sums[b] -= num
                        board_row_counts[b][r] += 1
                        board_col_counts[b][c] += 1
                        board_is_marked = True
                        break
                if board_is_marked:
                    break
            
            if WIN_COUNT in board_row_counts[b] or WIN_COUNT in board_col_counts[b]:
                won_boards.append(b)
        
        if len(won_boards) == len(boards):
            b = won_boards[-1]
            winning_sum = board_sums[b]
            last_number = num_called
            break

    score = winning_sum * last_number

    # When using 'sample.in' data:
    # if winning_sum == 148 and last_number == 13 and score == 1924:
    #     print('SUCCESS')
    # else:
    #     print('FAILURE')
    
    print(f'    Sum = {winning_sum}, Last number called = {last_number}')
    print(f'    ==> Score = {score}\n')


if __name__ == '__main__':
    filename = 'input.in'
    numbers_called, boards = parse(filename)

    # part_one(numbers_called, boards)

    part_two(numbers_called, boards)
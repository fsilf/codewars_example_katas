# CodeWars Kata Rank04: Connect Four
# You will receive a list of strings showing the order of the pieces which dropped in columns.
# The first player who connects four items of the same color is the winner.
# See full description and constrains of the kata at codewar:
# https://www.codewars.com/kata/56882731514ec3ec3d000009/python

import re

def check_diagonals(strng, pat):
    # check diagonals 1
    diags = ''
    for num in [0,1,2,3,7,14]:
        i = 0
        while True:
            t_sum = num + 8 * i 
            if t_sum <= 41:
                diags = ''.join([diags, strng[t_sum]])
                i += 1
            else:
                diags += ' ' 
                break
    # check diagonals 2
    for num, sum_min in zip([21, 28, 35, 36, 37, 38], [3, 4, 5, 6, 13, 20]):
        i = 0
        while True:
            t_sum = num - 6 * i 
            if t_sum >= sum_min:
                diags = ''.join([diags, strng[t_sum]])
                i += 1
            else:
                diags += ' ' 
                break
                
    if pat.search(diags) is not None:
        return 'win'
    
def who_is_winner(pieces_position_list):
    
    # dictionaries to convert and keep tract of the moves
    columns = {letter:num for letter, num in zip([*'ABCDEFGG'], [*'0123456'])}
    moves_mem = {num:5 for num in [*'0123456']}  
    # pattern to convert the moves
    convert = lambda match: columns[match.group(1)]
    move_pattern = re.compile('([ABCDEFG])_.*$')
    # pattern to win
    four_pattern = re.compile('OOOO|XXXX')    
    # create base board
    board = 'E' * 42
    # get first player
    player = 'O' if pieces_position_list[0].split('_')[1] == 'Yellow' else 'X'

    # moves
    for move in pieces_position_list:
        # record move
        move = move_pattern.sub(convert,move)
        pos = int(move) + moves_mem[move] * 7
        board = board[:pos] + player + board[pos + 1:]
        moves_mem[move] -= 1

        # check rows and columns
        current_rows = [board[i: i + 7] for i in [0,7,14,21,28,35]]
        current_columns = [''.join(x) for x in zip(*current_rows)]
        if four_pattern.search(' '.join([*current_rows, *current_columns])) is not None:
            return 'Red' if player == 'X' else 'Yellow'

        # check diagonals
        if check_diagonals(board, four_pattern) is not None:
            return 'Red' if player == 'X' else 'Yellow'
        # assign next player
        player = 'O' if player == 'X' else 'X'
    return 'Draw'

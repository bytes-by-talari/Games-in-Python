
# ai.py

import random
from tic_tac_toe import *


def random_ai(empty_spots):
    if len(empty_spots) > 1:
        random_num = random.randint( 1, len(empty_spots) )
        return int( empty_spots[random_num - 1] )
    else:
        return 1

#return best position via min max search
def minimax(state, player):

    if player == "O":
        best = [-1, -float("inf")]
    else:
        best = [-1, float("inf")]

    empty_regions = find_empty_regions(state)

    if terminal_test_ai(state,'X'):
        return [-1, -10]
    if terminal_test_ai(state,'O'):
        return [-1, 10]
    if len(empty_regions) == 0:
        return [-1, 0]

    for region in empty_regions:
        state[int(region)] = str( player )
        score = minimax(state, get_opponent(player))
        state[int(region)] = str(region)
        score[0] = region
        if player == "O": 
            if score[1] > best[1]:
                best = score
        else:
            if score[1] < best[1]:
                best = score
    return best

# return best  position via full alpha-beta search
def alphabeta(state, alpha, beta, player):

    if player == "O":
        best = [-1, -float("inf")]
    else:
        best = [-1, float("inf")]

    empty_regions = find_empty_regions(state)

    if terminal_test_ai(state, 'X'):
        return [-1, -10]
    if terminal_test_ai(state, 'O'):
        return [-1, 10]
    if len(empty_regions) == 0:
        return [-1, 0]

    for region in empty_regions:
        state[int(region)] = str( player ) # update board state
        score = alphabeta(state, alpha, beta, get_opponent(player))
        state[int(region)] = str(region)
        score[0] = region
        if player == "O": # if player is "O"
            if score[1] > best[1]:
                best = score
            alpha = max(alpha, best[1])
            if beta <= alpha:
                break
        else: # is player is "X"
            if score[1] < best[1]:
                best = score
            beta = min(beta, best[1])
            if beta <= alpha:
                break
    return best

# return best  position via full alpha-beta search with cutoff
def alphabeta_cutoff(state, alpha, beta, depth, player):

    if player == "O":
        best = [-1, -float("inf")]
    else:
        best = [-1, float("inf")]

    empty_regions = find_empty_regions(state)

    if terminal_test_ai(state, 'X'):
        return [-1, -10]
    if terminal_test_ai(state, 'O'):
        return [-1, 10]
    if len(empty_regions) == 0:
        return [-1, 0]

    if depth == 3:
        result = alphabeta_eval(state) 
        return [-1, result]

    for region in empty_regions:
        state[int(region)] = str( player )
        score = alphabeta_cutoff(state, alpha, beta, depth + 1, get_opponent(player))
        state[int(region)] = str(region)
        score[0] = region
        if player == "O": 
            if score[1] > best[1]:
                best = score
            alpha = max(alpha, best[1])
            if beta <= alpha:
                break
        else:
            if score[1] < best[1]:
                best = score
            beta = min(beta, best[1])
            if beta <= alpha:
                break
    return best

# evaluation function
# look ahead two moves
# if number wins for x > o -> -10
# if number wins for o > x -> 10
# if number wins for x = o -> 0
def alphabeta_eval(state):
    
    empty_regions = find_empty_regions(state)
    

    score_o = 0
    player = "O"
    for i in empty_regions:
        state[int(i)] = str(player)
        empty_regions = find_empty_regions(state)
        for j in empty_regions:
            state[int(j)] = str(player)
            if three_in_a_row(state, player):
                score_o = score_o + 1
            state[int(j)] = str(j)
        state[int(i)] = str(i)

    score_x = 0
    player = "X"
    for i in empty_regions:
        state[int(i)] = str(player)
        empty_regions = find_empty_regions(state)
        for j in empty_regions:
            state[int(j)] = str(player)
            if three_in_a_row(state, player):
                score_x = score_x + 1
            state[int(j)] = str(j)
        state[int(i)] = str(i)

    if score_o > score_x:
        score = 10
    elif score_x > score_o:
        score = -10
    else:
        score = 0

    return score

# terminal test for ai
def terminal_test_ai(state, player):

    empty_regions = find_empty_regions(state)

    if (state[0] == player and state[1] == player and state[2] == player) or \
            (state[3] == player and state[4] == player and state[5] == player) or \
            (state[6] == player and state[7] == player and state[8] == player) or \
            (state[0] == player and state[3] == player and state[6] == player) or \
            (state[1] == player and state[4] == player and state[7] == player) or \
            (state[2] == player and state[5] == player and state[8] == player) or \
            (state[0] == player and state[4] == player and state[8] == player) or \
            (state[2] == player and state[4] == player and state[6] == player):
        return True

    elif len(empty_regions) == 0:

        return False

# check for three in a row for evaluation function
def three_in_a_row(state, player):

    if (state[0] == player and state[1] == player and state[2] == player) or \
            (state[3] == player and state[4] == player and state[5] == player) or \
            (state[6] == player and state[7] == player and state[8] == player) or \
            (state[0] == player and state[3] == player and state[6] == player) or \
            (state[1] == player and state[4] == player and state[7] == player) or \
            (state[2] == player and state[5] == player and state[8] == player) or \
            (state[0] == player and state[4] == player and state[8] == player) or \
            (state[2] == player and state[4] == player and state[6] == player):
        return True
    else:
        return False

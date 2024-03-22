import random


HUMAN = -1
COMP = +1
board = [0] * 9


def evaluate(state):
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score


def wins(state, player):
    win_state = [
        [state[0], state[1], state[2]],
        [state[3], state[4], state[5]],
        [state[6], state[7], state[8]],

        [state[0], state[3], state[6]],
        [state[1], state[4], state[7]],
        [state[2], state[5], state[8]],

        [state[0], state[4], state[8]],
        [state[2], state[4], state[6]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def game_over(state):
    if len(empty_cells(board)) <= 0:
        return True
    return wins(state, HUMAN) or wins(state, COMP)


def empty_cells(state):
    cells = []
    for cell in state:
        if cell == 0:
            cells.append(cell)
    return cells


def valid_move(cell):
    if cell in empty_cells(board):
        return True
    else:
        return False


def set_move(cell, player):
    if valid_move(cell):
        board[cell] = player
        return True
    else:
        return False


def minimax(state, depth, player):
    if player == COMP:
        best = [-1, -1, float('-inf')]
    else:
        best = [-1, -1, float('inf')]

    if game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        state[cell] = player
        score = minimax(state, depth - 1, -player)
        state[cell] = 0
        score[0] = cell

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value
    
    return best


def render(state, c_choice, h_choice):
    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    for row in state:
        for cell in row:
            symbol = chars[cell]
            if symbol != " ":
                print(f' {symbol} ', end='')
            else:
                print(" - ", end='')
        print()
    print()


def ai_turn(c_choice, h_choice):
    depth = len(empty_cells(board))
    if game_over(board):
        return

    print(f'Computer turn [{c_choice}]')

    if depth == 9:
        x = random.choice([0, 1, 2])
        y = random.choice([0, 1, 2])
    else:
        move = minimax(board, depth, COMP)
        x, y = move[0], move[1]

    set_move(x, y, COMP)
    render(board, c_choice, h_choice)


def human_turn(c_choice, h_choice):
    depth = len(empty_cells(board))
    if game_over(board):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }
    print(f'Human turn [{h_choice}]')

    while move < 1 or move > 9:
        try:
            move = int(input('Use numpad (1..9): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMAN)

            if not can_move:
                print('Already taken. Try Again')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Wrong choice. Try Again')
    render(board, c_choice, h_choice)


def main():
    h_choice = 'O'
    c_choice = 'X'

    render(board, c_choice, h_choice)
    # Main loop of this game
    while not game_over(board):
        human_turn(c_choice, h_choice)
        ai_turn(c_choice, h_choice)

    # Game over message
    if wins(board, HUMAN):
        print('YOU WIN!')
    elif wins(board, COMP):
        print('YOU LOSE!')
    else:
        print('DRAW!')

    exit()


if __name__ == '__main__':
    main()

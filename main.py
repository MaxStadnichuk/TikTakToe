def input_move():
    global row,column
    while True:
        row,column=input('Enter the coordinates: ').split()
        row = int(row)-1
        column=int(column)-1
        if row>3 or row<0 or column<0 or column>3:
            print('Error')
            input_move
        elif game_field[row][column]!='_':
            print('Error')
            input_move
        else:
            break
    return row,column

def print_field():
    for j in range(11):
        print('-', end='')
    print('', end='\n')
    for i in range(3):
        print('|', *[game_field[i][j] for j in range(3)], '|')
    for j in range(11):
        print('-', end='')
    print('', end='\n')

def check_winner():
    win = None

    # checking rows
    for i in range(3):
        win = True
        for j in range(3):
            if game_field[i][j] != current_player:
                win = False
                break
        if win:
            return current_player

    # checking columns
    for i in range(3):
        win = True
        for j in range(3):
            if game_field[j][i] != current_player:
                win = False
                break
        if win:
            return current_player

    # checking diagonals
    win = True
    for i in range(3):
        if game_field[i][i] != current_player:
            win = False
            break
    if win:
        return current_player

    win = True
    for i in range(3):
        if game_field[i][3 - 1 - i] != current_player:
            win = False
            break
    if win:
        return current_player
    return None

def tie_checking():
    t = True
    for i in range(3):
        for j in range(3):
            if game_field[i][j]=='_':
                t = False
    return t

def congratulate_player(a):
    print(f'Congratulations! The winner is {a}')




first_player = 'X'
second_player = 'O'

game_field = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

# first player is first to make a move
current_player = first_player
while True:
    row, column = input_move()
    game_field[row][column] = current_player
    print_field()
    winner = check_winner()
    tieee = tie_checking()


    if tieee is True:
        print('Tie')
        b = input('Do you want to play again?(1-yes,2-no)')
        if b == '2':
            quit()
        elif b == '1':
            game_field = [
                ["_", "_", "_"],
                ["_", "_", "_"],
                ["_", "_", "_"],
                ["_", "_", "_"]
            ]
            break


    if winner is not None:
        congratulate_player(winner)
        b=input('Do you want to play again?(1-yes,2-no)')
        if b == '2':
            quit()
        elif b == '1':
            game_field = [
                ["_", "_", "_"],
                ["_", "_", "_"],
                ["_", "_", "_"],
                ["_", "_", "_"]
            ]
            continue




    current_player = first_player if current_player == second_player else second_player


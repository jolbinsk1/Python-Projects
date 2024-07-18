import random
from IPython.display import clear_output

def display_board(board):
    clear_output()
    
    print(' -----------')
    print('|   |   |   |')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('|   |   |   |')
    print(' -----------')
    print('|   |   |   |')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('|   |   |   |')
    print(' -----------')    
    print('|   |   |   |')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('|   |   |   |')
    print(' -----------')

def player_info():
    username_1 = ''
    username_2 = ''
    while username_1 == '':
        username_1 = input('Please enter your username: ')
    while username_2 == '':
        username_2 = input('Please enter your username: ')
    
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Please enter either X or O: ').upper()
    if marker == 'X':
        return (f'{username_1}','X',f'{username_2}', 'O')
    else:
        return (f'{username_1}','O',f'{username_2}', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win(board, marker):
    return(
    (board[1] == board[2] == board[3] == marker) or 
    (board[4] == board[5] == board[6] == marker) or 
    (board[7] == board[8] == board[9] == marker) or 
        
    (board[1] == board[4] == board[7] == marker) or 
    (board[2] == board[5] == board[8] == marker) or 
    (board[3] == board[6] == board[9] == marker) or 
        
    (board[1] == board[5] == board[9] == marker) or 
    (board[3] == board[5] == board[7] == marker)  
    )

def first_turn(username_1,username_2):
    if random.randint(0,1)==0:
        return '{} goes first'.format(username_1)
    else:
        return '{} goes first'.format(username_2)

def empty_space(board,position):
    return board[position] == ' '

def player_turn(board):
    position = ''
    while position not in range(9) or not empty_space(board,position):
        position = int(input('Please enter your next move (1-9): '))

def full_board_check(board):
    for x in range(9):
        if empty_space(board,x):
            return False
    return True

# Now for the actual game!

while True:

    game_on = True
    board = [' '] * 9
    username_1, p1_marker username_2, p2_marker = player_info()
    turn_one = first_turn(username_1,username_2)
    print(turn_one + ' goes first')
    
    lets_play = input('Wanna play Tic Tac Toe? Enter Y or N: ')
    
    if lets_play[0].lower()=='y':
        game_on = True
    else:
        game_on = False
    
    while game_on: 
        if turn_one == username_1:
            display_board(board)
            position = player_turn(the_board)
            place_marker(board, p1_marker, position)
            
            if win_check(board, p1_marker):
                display_board(board)
                print('Congratulations {}, you win!'.format(username_1))
                game_on = False
            else:
                if full_board_check(board,position):
                    display_board(board)
                    print("It's a tie!")
                    break
                else:
                    turn = username_2
        else:
            display_board(board)
            position = player_turn(board)
            place_marker(board,p2_marker, position)
            
            if win_check(board, p2_marker):
                display_board(board)
                print('Congratulations {}, you win!'.format(username_2))
                game_on = False
            else:
                if full_board_check(board, position):
                    display_board(board)
                    print("It's a tie!")
                    break
                else:
                    turn = username_1
    
    another_round = input('Wanna play again? Enter Y or N: )
        if another_round[0].lower()=='y':
            game_on = True
            continue
        elif another_round[0].lower()=='n':
            print('Goodbye!')
            break
        else:
            print('Please enter either Y or N: ')
            continue
        break
        

  





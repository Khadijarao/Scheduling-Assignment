

boxes = [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
first_player = 'X'
turn = 1
winning_combos = [  [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                    [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6], ]

def print_board(initial=False):
   
    print('''
             {} | {} | {} 
            -----------
             {} | {} | {}
            -----------
             {} | {} | {} 
        ''').format(*([x for x in range(1, 10)] if initial else boxes))

def take_turn(player, turn):
   
    while True:
        box = raw_input('Player %s, type a number from 1-9 to select a box: ' % player)

        try:
            box = int(box) - 1
            if 0 <= box <= 8:
                if boxes[box] == ' ': # initial value
                    boxes[box] = player # set to value of current player
                    break
                else:
                    print('That box is already marked, try again.\n')
                    continue
            else:
                print('That number is out of range, try again.\n')
                continue

        except ValueError:
            # Not an integer
            print('That\'s not a valid number, try again.\n')
            continue

def switch_player(turn):
   
    current_player = '0' if turn % 2 == 0 else 'X'
    return current_player

def check_for_win(player, turn):
   
    win = False
    tie = False
    if turn > 4: # need at least 5 moves before a win is possible
        for x in range(len(winning_combos)):
            score = 0
            for y in range(len(winning_combos[x])):
                if boxes[winning_combos[x][y]] == player:
                    score += 1
                if score == 3:
                    win = True

        if turn == 9:
            tie = True

    return win, tie

def play(player, turn):
   
    while True:
        take_turn(player, turn)
        print_board()
        win, tie = check_for_win(player, turn)
        if win or tie:
            if win:
                print('Game over. %s wins!\n' % player)
            else:
                print('Game over. It\'s a tie.\n')
            break
        turn += 1
        player = switch_player(turn)

# Begin the game: 
print('\n\nWelcome to Tic Tac Toe for two humans!')
print_board(initial=True)
play(first_player, turn)
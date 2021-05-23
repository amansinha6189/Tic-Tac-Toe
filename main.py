#

#Board
# Display Board
# play Game
# check win
    # check rows
    #check columns
    # check diagonals
# check tied
# flip player

# ------------- Global VAriables------------
# Board
board = ["-","-","-",
         "-","-","-",
         "-","-","-",]
# if game is still running,
game_still_running = True

# Who won or tie
winner = None

# whose turn 
current_player = "X"



# ---------------- GAME ---------------- 
def display_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])
    
# play Game of tic tak toe
def play_game():
    
    #Display initial Board
    display_board()
    
    # while the game is not over
    while game_still_running:
        # handle a single tuirn of an arbitrary player
        handle_turn(current_player)
        
        
        # check if the game has ended
        check_if_game_over()
        
        # Flip to The other Player
        flip_player()
        
        # The game has ended
        if winner == "X" or winner == "O":
            print(winner+" won.")
        elif winner == None:
            print("Tie.")
    
    
def handle_turn(player):
    print(player + "'s Turn.")
    position = input("Choose a position from 1-9: ")
    
    
    valid = False
    while not valid:
        while position not in ["1",'2','3','4','5','6','7','8','9']:
            position = input("invalid Input \nChoose a position from 1-9: ")
        position = int(position) - 1
        
        if board[position] == "-":
            valid =True
        else:
            print("you can't go there again. Try again")
    board[position] = player
    display_board()
    
    
    
def check_if_game_over():
    check_for_winner()
    check_if_tie()
    
def check_for_winner():
    # setting up global variables
    global winner
    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()
    
    if row_winner:
        # there was a win
        winner = row_winner
    elif column_winner:
        # there was a win
        winner = column_winner
        
    elif diagonal_winner:
        # There was a win
        winner = diagonal_winner
    else:
        #no win
        winner = None;
    return


def check_rows():
    global game_still_running
    row_1 = board[0]==board[1]==board[2] != "-"
    row_2 = board[3]==board[4]==board[5] != "-"
    row_3 = board[6]==board[7]==board[8] != "-"
    
    if row_1 or row_2 or row_3:
        game_still_running =False
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return

def check_columns():
    global game_still_running
    column_1 = board[0]==board[3]==board[6] != "-"
    column_2 = board[1]==board[4]==board[7] != "-"
    column_3 = board[2]==board[5]==board[8] != "-"
    
    if column_1 or column_2 or column_3:
        game_still_running =False
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return

def check_diagonals():
    global game_still_running
    diagonal_1 = board[0]==board[4]==board[8] != "-"
    diagonal_2 = board[2]==board[4]==board[6] != "-"

    
    if diagonal_1 or diagonal_2:
        game_still_running =False
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[2]

    return


def check_if_tie():
    global game_still_running
    if "-" not in board:
        game_still_running = False
    return

def flip_player():
    global current_player
    if current_player =="X":
        current_player = "O"
    elif current_player =="O":
        current_player = "X"
    return

    




play_game()
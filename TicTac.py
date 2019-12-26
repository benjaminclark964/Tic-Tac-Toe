# Author: Benjamin Clark


from random import randrange


j = 0
boardCount = 0
row, col = (5, 5)
board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]


# main function
def main():
    play_game()


# start the game
def play_game():
    initialize_board()
    t = turn()
    current_board(board)
    # keeps the game running until it is over
    while check_win(board) == -1 and check_stalemate(board) != 0:
        if t == '0':
            user_value = ai_hard(board)    # AI turn in future
            print(user_value)
            # checks that move is valid
            if new_board(user_value, t) == -1:
                continue
            t = '1'
        else:
            user_value = user_turn()
            # checks that move is valid
            if new_board(user_value, t) == -1:
                continue
            t = '0'
        current_board(board)
    play_game()


# function for player to decide who plays first
def turn():
    t = input("0 for AI to go first, anything else for user")
    return t


# function initializing the board
def initialize_board():
    j = 0
    for i in board:
        board[j] = '_'
        j = j+1


# function to exit program
def exit_game(user_val):
    if user_val == 'q':
        exit(0)


# function creating a new game if the user enters "n"
def new_game(user_val):
    if user_val == "n":
        play_game()


# function to fill array with valid values
def current_board(cur):
    print("Enter n for new game or q to quit")
    print("1|2|3\t" + cur[0] + "|" + cur[1] + "|" + cur[2])
    print("4|5|6\t" + cur[3] + "|" + cur[4] + "|" + cur[5])
    print("7|8|9\t" + cur[6] + "|" + cur[7] + "|" + cur[8])
    return cur


# function returning the index the user chose
def user_turn():
    val = -2
    user_val = input("Enter Move")
    exit_game(user_val)  # exit game if user enters "q
    new_game(user_val)   # new game if user enters "n"
    while not user_val.isdigit():
        print("Enter number between 1-9 for move")
        user_val = input("Enter Move")
    while val == -2:
        while (int(user_val) < 0 or int(user_val) > 9) and user_val.isdigit():
            print("Invalid move")
            user_val = input("Enter Move")
        val = int(user_val)

    return val


# Adds new move to the board
def new_board(index, user):
    val = index-1
    return_val = 0
    if user != '0':
        if board[val] == '_':
            board[val] = 'X'
        else:
            print("Invalid move")
            return_val = -1
    elif user == '0':
        if board[val] == '_':
            board[val] = 'O'
        else:
            print("Invalid move")
            return_val = -1
    return return_val


# function to allow board positions to be checked quickly for winning conditions
def board_check(cur, i, j, k):
    if cur[i] == cur[j] == cur[k] and cur[i] == 'X':
        print("Congratulations user, you win!")
        return 0
    elif cur[i] == cur[j] == cur[k] and cur[i] == 'O':
        print("AI wins")
        return 0
    else:
        return -1


# checks if stalemate has occurred
def check_stalemate(cur):
    empty_spaces = 0
    for elem in cur:
        if elem == '_':
            empty_spaces = empty_spaces+1
    if empty_spaces == 0:
        print("Stalemate!")
    return empty_spaces


# checks if the game has been won
def check_win(cur):
    val = -1
    if board_check(cur, 0, 1, 2) == 0:
        val = 0
    if board_check(cur, 0, 3, 6) == 0:
        val = 0
    if board_check(cur, 0, 4, 8) == 0:
        val = 0
    if board_check(cur, 1, 4, 7) == 0:
        val = 0
    if board_check(cur, 2, 5, 8) == 0:
        val = 0
    if board_check(cur, 2, 4, 6) == 0:
        val = 0
    if board_check(cur, 3, 4, 5) == 0:
        val = 0
    if board_check(cur, 6, 7, 8) == 0:
        val = 0
    return val


# ############################################## AI Code #########################################

# AI random move
def random_move():
    ai_index = randrange(9)
    return ai_index


# AI functionality
def ai_hard(cur):
    score = 0
    max_score = 0
    move = 0
    block_win = -1

    for i in range(0, 9):
        if cur[i] == '_':
            if i != 0 and i != 3 and i != 6 and cur[i-1] == 'O':    # left
                score = score+1
            if i != 2 and i != 5 and i != 8 and cur[i+1] == 'O':    # right
                score = score+1
            if i != 0 and i != 1 and i != 3 and i != 7 and cur[i-2] == 'O' and cur[i-1] != 'X':     # left other-side
                score = score+1
            if i != 1 and i != 5 and i != 7 and i != 8 and cur[i+2] == 'O' and cur[i+1] != 'X':     # right other-side
                score = score+1
            if (i == 0 or i == 4) and cur[i+4] == 'O':  # diagonal down-right
                score = score+1
            if (i == 8 or i == 4) and cur[i-4] == 'O':  # diagonal up-left
                score = score+1
            if i != 6 and i != 7 and i != 8 and cur[i+3] == 'O':    # downward
                score = score+1
            if i != 0 and i != 1 and i != 2 and cur[i-3] == 'O':    # upward
                score = score+1

            # additional checks to ensure an X is not present to block a win and therefore not add a point
            if i == 6 and cur[i-4] == 'O' and cur[4] != 'X':
                score = score+1
            if i == 2 and cur[i+4] == 'O' and cur[4] != 'X':
                score = score+1
            if i == 0 and cur[i+8] == 'O' and cur[4] != 'X':
                score = score+1
            if i == 8 and cur[i-8] == 'O' and cur[4] != 'X':
                score = score+1
            if i == 0 and cur[i+6] == 'O' and cur[3] != 'X':
                score = score+1
            if i == 6 and cur[i-6] == 'O' and cur[3] != 'X':
                score = score+1
            if i == 2 and cur[i+6] == 'O' and cur[5] != 'X':
                score = score+1
            if i == 8 and cur[i-6] == 'O' and cur[5] != 'X':
                score = score+1
            if score == 0:
                max_score = score
                move = random_move()
            else:
                if score > max_score:
                    if score == 2:
                        if ai_win(cur, i) == 0:
                            move = i+1
                            return move
                    max_score = score
                    move = i
            if check_if_player_is_going_to_win(board, i) == 2:
                block_win = i+1
            score = 0
    if block_win != -1:
        return block_win
    else:
        return move+1


# Check if player is going to win
def check_if_player_is_going_to_win(cur, i):
        score = 0

        if cur[i] == '_':
            if i != 0 and i != 3 and i != 6 and cur[i - 1] == 'X':
                score = score + 1
            if i != 2 and i != 5 and i != 8 and cur[i + 1] == 'X':
                score = score + 1
            if i != 0 and i != 1 and i != 3 and i != 7 and cur[i - 2] == 'X':
                score = score + 1
            if i != 1 and i != 5 and i != 7 and i != 8 and cur[i + 2] == 'X':
                score = score + 1
            if (i == 0 or i == 4) and cur[i + 4] == 'X':
                score = score + 1
            if (i == 8 or i == 4) and cur[i - 4] == 'X':
                score = score + 1
            if i != 6 and i != 7 and i != 8 and cur[i + 3] == 'X':
                score = score + 1
            if i != 0 and i != 1 and i != 2 and cur[i - 3] == 'X':
                score = score + 1
            if i == 6 and cur[i - 4] == 'X' and cur[4] != 'O':
                score = score + 1
            if i == 2 and cur[i + 4] == 'X' and cur[4] != 'O':
                score = score + 1
            if i == 0 and cur[i + 8] == 'X' and cur[4] != 'O':
                score = score + 1
            if i == 8 and cur[i - 8] == 'X' and cur[4] != 'O':
                score = score + 1
            if i == 0 and cur[i + 6] == 'X' and cur[3] != 'O':
                score = score + 1
            if i == 6 and cur[i - 6] == 'X' and cur[3] != 'O':
                score = score + 1
            if i == 2 and cur[i + 6] == 'X' and cur[5] != 'O':
                score = score + 1
            if i == 8 and cur[i - 6] == 'X' and cur[5] != 'O':
                score = score + 1

        if score == 2:
            if player_win(cur, i) == 0:
                return score
            else:
                return -1
        else:
            return -1


# Verify player is going to win
def player_win(cur, index):
    return_val = -1
    copy = cur
    copy[index] = 'X'
    if check_win(copy) == 0:
        return_val = 0
    copy[index] = '_'
    return return_val


# Verify AI is going to win
def ai_win(cur, index):
    return_val = -1
    copy = cur
    copy[index] = 'O'
    if check_win(copy) == 0:
        return_val = 0
    copy[index] = '_'
    return return_val


# starting the main function
main()

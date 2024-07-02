# ANSI escape codes for colors
class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    END = '\033[0m'

# # Example usage
# today = (colors.RED + "∎" + colors.END)
# print(today)
# print(colors.BLUE + "This text is blue!" + colors.END)

def create_board(width, height):
    board = []
    for _ in range(height):
        row = []
        row.extend([0]*width)
        board.append(row)
    return board

def display_board(board,player1_color,player2_color):
    # TODO: we can import this color_key later when calling this function with custom colors 
    #       or import the players color and replace YELLOW, RED with that variable 
    color_key = {
        0:" ",
        1:(player1_color + "●" + colors.END),
        2:(player2_color + "●" + colors.END)
    }
    # NOTE: There can only be values in the board that are values in the color key or else error 

    # Print the matching numbers to columns on top 
    for k in range(len(board[0])):
        print(" " + str(k) + " ",end='')
    print()


    # Go through the board item by item 
    for i in range(len(board)):
        for j in range(len(board[i])):
            # Master item is the value of the actuall board
            master_item = board[i][j]

            # Display item is the colored facy peice the master item traslates to 
            display_item = color_key[master_item]
            # Print that item in its spot on the board 
            print('[' + display_item + ']',end='')
        print()

def pre_game():
    board_width = 7
    board_height = 6
    print(f"Demensions of board: {board_width},{board_height}")
    player1_color = colors.YELLOW
    player1_peice = (player1_color + "●" + colors.END)
    player2_color = colors.RED
    player2_peice = (player2_color + "●" + colors.END)
    print(f'Player 1 Color: Yellow {player1_peice} \nPlayer 2 Color: Red {player2_peice}')
    print('Starting game now...\n\n')

    game(board_width,board_height,player1_color,player2_color)

def game(board_width,board_height,player1_color,player2_color):
    board = create_board(board_width,board_height)
    game_over = False
    while not game_over:
        display_board(board,player1_color,player2_color)
        #get_valid_move()
        #Update the master board()
        #Check for win 
        # which players 
        game_over = True



if __name__ == '__main__':
    pre_game()


'''
RULES:
    1. color1 & color2 variables have to be a color inside the colors class
'''


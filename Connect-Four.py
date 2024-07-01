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

def create_board():
    # TODO: Not used yet 
    board_width = 7
    board_height = 6
    board = [
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,1,2,0,0,0],
        [0,1,2,2,1,2,2]
        ]
    return board

def display_board(board):
    # TODO: we can import this color_key later when calling this function with custom colors 
    #       or import the players color and replace YELLOW, RED with that variable 
    color_key = {
        0:" ",
        1:(colors.YELLOW + "●" + colors.END),
        2:(colors.RED + "●" + colors.END),
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

def game():
    # TODO: think about the process of this before coding 

board = create_board()
display_board(board)


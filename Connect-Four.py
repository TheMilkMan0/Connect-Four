import os 
import sys 

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
    '''
    This function will return a list of lists where the length of the list 
    will be the [hight] and the lenght of the sublists will be the [width]

    :param width: the width of the 'board' or the length of the sublists
    :type width: int
    :param height: the height of the 'board' or the length of the main list
    :type height: int

    :rtype: list 
    :return: a 2d list filled with integer zeros that represent the connect 4 board 
    '''
    board = []
    for _ in range(height):
        row = []
        row.extend([0]*width)
        board.append(row)
    return board

def display_board(board):
    color_key = {
        0:" ",
        1:(colors.YELLOW + "●" + colors.END),
        2:(colors.RED + "●" + colors.END)
    }
    # NOTE: Color Key keys can only be values in the board that are values in the color key or else error 
    #       You could have multiple players in the future if you 

    # Print the matching numbers to columns on top 
    for k in range(1,len(board[0])+1):
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

## CHAT GPT CODE ##
def get_key():
    if os.name == 'nt':
        import msvcrt
        return msvcrt.getch().decode('utf-8')
    else:
        import tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return key
## END OFF CHAT GPT CODE ##

def get_valid_move(board):
    '''
    This function will ask the user to press a key to represent 
    the column they wish to have their peice placed. 
    The visual columns presented to the user start with the number 1. 
    while the return value of this function will be ajusted for the column chosen to be in index form. 

    :param board: the master board (2d List) with integers stored as players peices locations
    :type board: list (2d list)

    :rtype: int
    :return: integer representing column converted in the index form of the master board 
    '''
    # Constatnly Run until the user has a proper selection 
    while True:
        # use try here because the program will try to convert the user input to a integer 
        try:
            print(("Enter column (1-7): "))
            # Use the get_key function to instantly get the integer of the key pressed without the user having to press enter 
            column = int(get_key()) - 1
            # if the integer pressed is inside the culumn bounds of the board and the top most place of the column does not have a peice in it then continue 
            if 0 <= column < len(board[0]) and board[0][column] == 0:
                return column
            # if the integer is to large or small 
            else:
                print("Invalid move. Try again.")
        # if the key press was not a integer at all 
        except:
            print("Please enter a valid integer.")

def forward_check(i,j,peice_num,board):
    '''
    This function will check for [required_in_a_row] in a row. 
    Customize: [required_in_a_row] can be changed to any number, 1 in a row will presumably end instantly
    
    :param i: the row (sublist) we are in on the board
    :type i: int
    :param j: the column (index) we are in on the row of the board
    :type j: int
    :param peice_num: the integeger representing the player on the master board 
    :type peice_num: int
    :param board: the master board (2d list) with integers as players
    :type board: list

    :rtype: boolean
    :return: True for win, False for no Win

    '''
    required_in_a_row = 3
    # ----------------------
    # Define a counter for tracking how many are cuently in a row from the starting point of i,j
    peice_in_row_count = 1
    # Count how many times we have moved forward 
    move_forward_count = 1
    # cut down on the number of checks by returning a auto false if the checking postion is at the end of the row, its not possible to have 4 in a row if the starting position is the 3rd from last position of the row 
    if peice_num == 0:
        return False
    if j > len(board[i])-required_in_a_row:
        return False
    
    # from the starting point check ahead [required_in_a_row] times
    for _ in range(required_in_a_row-1):

        # check that the next checking possiion is within bounds
        if j + move_forward_count < len(board[i]):

            # if the peice to the right (however many right) is the same as the to be checked peice then add to [peice_in_a_row] counter
            if board[i][j+move_forward_count] == peice_num:
                peice_in_row_count += 1

                # if there were [required_in_a_row] in a row then call a win 
                if peice_in_row_count >= required_in_a_row:

                    # a return of true means there where 4 peices in a row 
                    return True
            # Cut this function short by return false (lose) after there wasnt another in a row, because if we are only checking [required_in_a_row] times then all of those times have to be true for it to be a win                 
            else:
                return False
            move_forward_count += 1

def game():
    board = create_board(7,6)
    game_over = False
    while not game_over:
        display_board(board)
        # This variable is in the list index form (min being zero)
        column = get_valid_move(board) 
        #Update the master board()
        #Check for win 
        # which players 
        game_over = True



if __name__ == '__main__':
    game()


'''
RULES:
    1. color1 & color2 variables have to be a color inside the colors class
'''


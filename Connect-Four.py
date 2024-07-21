import os 
import sys 
import time

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

def return_color_key() -> dict[int,str]:
    # NOTE: Color Key keys can only be values in the board that are values in the
    #  color key or else error 
    return {
            0:" ",
            1:(colors.YELLOW + "●" + colors.END),
            2:(colors.RED + "●" + colors.END),
            3:(colors.GREEN + "●" + colors.END),
            4:(colors.BLUE + "●" + colors.END),
            5:(colors.PURPLE + "●" + colors.END),
            6:(colors.CYAN + "●" + colors.END)
        }

def create_board(width: int, height: int) -> list[int]:
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
    board: list = []
    for _ in range(height):
        row = []
        row.extend([0]*width)
        board.append(row)
    return board

def display_board(board: list[int]):
    color_key = return_color_key()
    # Clear the consolor the print the new board
    os.system('cls' if os.name == 'nt' else 'clear')
    # Print the matching numbers to columns on top 
    for k in range(1,len(board[0])+1):
        print(" " + str(k) + " ",end='')
    print()


    # Go through the board item by item 
    for i in range(len(board)):
        for j in range(len(board[i])):
            # Master item is the value of the actuall board
            master_item: int = board[i][j]

            # Display item is the colored facy peice the master item traslates to 
            display_item: str = color_key[master_item]
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

def get_valid_move(board: list[int]) -> int:
    '''
    This function will ask the user to press a key to represent 
    the column they wish to have their peice placed. 
    The visual columns presented to the user start with the number 1. 
    while the return value of this function will be ajusted for the column chosen
      to be in index form. 

    :param board: the master board (2d List) with integers stored as players
      peices locations
    :type board: list (2d list)

    :rtype: int
    :return: integer representing column converted in the index form of the 
    master board 
    '''
    # Constatnly Run until the user has a proper selection 
    while True:
        # use try here because the program will try to convert the user input 
        # to a integer 
        try:
            print(("Enter column (1-7): "))
            # Use the get_key function to instantly get the integer of the key
            #  pressed without the user having to press enter 
            column: int = int(get_key()) - 1
            # if the integer pressed is inside the culumn bounds of the board 
            # and the top most place of the column does not have a peice in it
            # then continue 
            if 0 <= column < len(board[0]) and board[0][column] == 0:
                return column
            # if the integer is to large or small 
            else:
                print("Invalid move. Try again.")
        # if the key press was not a integer at all 
        except:
            print("Please enter a valid integer.")

def animate_placement(board: list[int], i: int, column: int, player: int) -> None:
    '''
    This function will receive the cords of the new placed peice, along with the player integer.
    Then it will animate the placement of that piece 

    :param board: the master board (2d List) with integers stored as players
      peices locations
    :type board: list (2d list)
    :param i: the row (sublist) on the board (2d list) where the peice was placed
    :type i: int
    :param column: the column (index) in the sublist on the board (2d list) where the peice was placed 
    :type column: int
    :param player: the integeger representing the player on the master board 
    :type player: int
    '''
    # get the color key to pull the players color 
    color_key: dict[int,str] = return_color_key()
    ## CUSTOMIZEABLE ##
    # the time delay before animating the next peace.
    animate_delay: float = 0.2
    # copy the list so we dont mess with the main board 
    copy_board = board
    # update the copy of the board which will animate the placement 
    for j in range(i):
        copy_board[j][column] = player
        display_board(copy_board)
        time.sleep(animate_delay)
        copy_board[j][column] = 0

def update_board(column: int, board: list[int], player: int) -> list[int]:
    # Start at the bottom of the board [len(board)-1] and
    #  then work your way up [Step: -1] then stop at zero (the top most position on the board)
    for i in range(len(board)-1,-1,-1):
            # If the row we are currently on has a [0] in the column of the users chosing
            # then change that possition on the board to the players digit
            if board[i][column] == 0:
                animate_placement(board,i,column,player)
                board[i][column] = player
                # Now that we found the corrext spot we willl use it to animate the peice dropping to that spot
                return board




def forward_check(i: int, j: int, peice_num: int, board: list[int], required_in_a_row: int) -> bool:
    '''
    This function will check for [required_in_a_row] in a row. 
    
    :param i: the row (sublist) we are in on the board
    :type i: int
    :param j: the column (index) we are in on the row of the board
    :type j: int
    :param peice_num: the integeger representing the player on the master board 
    :type peice_num: int
    :param board: the master board (2d list) with integers as players
    :type board: list
    :param required_in_a_row: the number of peices that are required to be in a row for it to count as a win
    :type required_in_a_row: int

    :rtype: boolean
    :return: True for win, False for no Win

    '''
    # ----------------------
    # Define a counter for tracking how many are cuently in a row from the starting
    #  point of i,j
    peice_in_row_count: int = 1

    # Count how many times we have moved forward 
    move_forward_count: int = 1

    # cut down on the number of checks by returning a auto false if the checking
    #  postion is at the end of the row, its not possible to have 4 in a row if
    #  the starting position is the 3rd from last position of the row 
    if j > len(board[i])-required_in_a_row:
        return False
    
    # from the starting point check ahead [required_in_a_row] times
    for _ in range(required_in_a_row-1):

        # check that the next checking possiion is within bounds
        if j + move_forward_count < len(board[i]):

            # if the cords have the same num as peice_num AND
            # if the peice to the right (however many right) is the same as the 
            # to be checked peice [peice_num] then add to [peice_in_a_row] counter
            if board[i][j] == peice_num and board[i][j+move_forward_count] == peice_num:
                peice_in_row_count += 1

                # if there were [required_in_a_row] in a row then call a win 
                if peice_in_row_count >= required_in_a_row:

                    # a return of true means there where 4 peices in a row 
                    return True
            # Cut this function short by return false (lose) after there wasnt
            #  another in a row, because if we are only checking 
            # [required_in_a_row] times then all of those times have to be true
            #  for it to be a win                 
            else:
                return False
            move_forward_count += 1


def virtical_check(i: int, j: int, peice_num: int, board: list[int], required_in_a_row: int) -> bool:
    '''
    This function will check for [required_in_a_row] in a column.
    
    :param i: the row (sublist) we are in on the board
    :type i: int
    :param j: the column (index) we are in on the row of the board
    :type j: int
    :param peice_num: the integeger representing the player on the master board 
    :type peice_num: int
    :param board: the master board (2d list) with integers as players
    :type board: list
    :param required_in_a_row: the number of peices that are required to be in a row for it to count as a win
    :type required_in_a_row: int

    :rtype: boolean
    :return: True for win, False for no Win

    '''
    # Define a counter for tracking how many are cuently in a row from the starting
    #  point of i,j
    peice_in_row_count: int = 1

    # Count how many times we have moved forward 
    move_forward_count: int = 1

   # cut down on the number of checks by returning a auto false if the checking
    #  postion is at the bottom of the column, its not possible to have 4 in a row if
    #  the starting position is the 3rd from last position of the column (top to bottom) 
    if i > len(board)-required_in_a_row:
        return False
    
    # from the starting point check ahead [required_in_a_row] times
    for _ in range(required_in_a_row-1):

        # check that the next checking possiion is within bounds
        if i + move_forward_count < len(board):
            # if the cords have the same num as peice_num AND
            # if the peice to the bottom (however many down) is the same as the 
            # to be checked peice [peice_num] then add to [peice_in_a_row] counter
            if board[i][j] == peice_num and board[i+move_forward_count][j] == peice_num:
                peice_in_row_count += 1

                # if there were [required_in_a_row] in a row then call a win 
                if peice_in_row_count >= required_in_a_row:

                    # a return of true means there where 4 peices in a row 
                    return True
            # Cut this function short by return false (lose) after there wasnt
            #  another in a row, because if we are only checking 
            # [required_in_a_row] times then all of those times have to be true
            #  for it to be a win                 
            else:
                return False
            move_forward_count += 1


def to_right_diagonal_check(i: int, j: int, peice_num: int, board: list[int], required_in_a_row: int) -> bool:
    '''
    This function will check for [required_in_a_row] in a diagonal starting from top left to bottom right.
    
    :param i: the row (sublist) we are in on the board
    :type i: int
    :param j: the column (index) we are in on the row of the board
    :type j: int
    :param peice_num: the integeger representing the player on the master board 
    :type peice_num: int
    :param board: the master board (2d list) with integers as players
    :type board: list
    :param required_in_a_row: the number of peices that are required to be in a row for it to count as a win
    :type required_in_a_row: int

    :rtype: boolean
    :return: True for win, False for no Win

    '''
    # Define a counter for tracking how many are cuently in a row from the starting
    #  point of i,j
    peice_in_row_count: int = 1

    # Count how many times we have moved forward 
    move_forward_count: int = 1

   # cut down on the number of checks by returning a auto false if the checking
    #  postion is at the bottom of the diagonal, its not possible to have 4 in a row if
    #  the starting position is the 3rd from last position of the diagonal2 (top to bottom) 
    if i > len(board)-required_in_a_row or j > len(board[i])-required_in_a_row:
        return False
    
    # from the starting point check ahead [required_in_a_row] times
    for _ in range(required_in_a_row-1):

        # check that the next checking possiion is within bounds
        if i + move_forward_count < len(board) and j + move_forward_count < len(board[i]):
            # if the cords have the same num as peice_num AND
            # if the peice to the bottom (however many down) is the same as the 
            # to be checked peice [peice_num] then add to [peice_in_a_row] counter
            if board[i][j] == peice_num and board[i+move_forward_count][j+move_forward_count] == peice_num:
                peice_in_row_count += 1

                # if there were [required_in_a_row] in a row then call a win 
                if peice_in_row_count >= required_in_a_row:

                    # a return of true means there where 4 peices in a row 
                    return True
            # Cut this function short by return false (lose) after there wasnt
            #  another in a row, because if we are only checking 
            # [required_in_a_row] times then all of those times have to be true
            #  for it to be a win                 
            else:
                return False
            move_forward_count += 1


def to_left_diagonal_check(i: int, j: int, peice_num: int, board: list[int], required_in_a_row: int) -> bool:
    '''
    This function will check for [required_in_a_row] in a diagonal that goes top right to bottom left .
    
    :param i: the row (sublist) we are in on the board
    :type i: int
    :param j: the column (index) we are in on the row of the board
    :type j: int
    :param peice_num: the integeger representing the player on the master board 
    :type peice_num: int
    :param board: the master board (2d list) with integers as players
    :type board: list
    :param required_in_a_row: the number of peices that are required to be in a row for it to count as a win
    :type required_in_a_row: int

    :rtype: boolean
    :return: True for win, False for no Win

    '''
    # Define a counter for tracking how many are cuently in a row from the starting
    #  point of i,j
    peice_in_row_count: int = 1

    # Count how many times we have moved forward 
    move_forward_count: int = 1
    
    # from the starting point check ahead [required_in_a_row]-1 times because the starting position counts as one
    for _ in range(required_in_a_row-1):

        # check that the next checking possiion is within bounds (Reminder we are going top right to bottom left)
        if i + move_forward_count < len(board) and j - move_forward_count > -1: #(Make sure the column is before the far left side)

            # if the cords have the same num as peice_num AND
            # if the peice to the bottom-left (however many diagonal) is the same as the 
            # to be checked peice [peice_num] then add to [peice_in_a_row] counter
            if board[i][j] == peice_num and board[i+move_forward_count][j-move_forward_count] == peice_num:
                peice_in_row_count += 1

                # if there were [required_in_a_row] in a row then call a win 
                if peice_in_row_count >= required_in_a_row:

                    # a return of true means there where 4 peices in a row 
                    return True
            # Cut this function short by return false (lose) after there wasnt
            #  another in a row, because if we are only checking 
            # [required_in_a_row] times then all of those times have to be true
            #  for it to be a win                 
            else:
                return False
            move_forward_count += 1
        else:
            break

def check_for_win(player: int, board: list[int], required_in_a_row: int) -> bool:
    '''
    This function will itterate over the board, passing the cords to the
      different ways to win functions who will check for their respective wins
      Forward, Diagonal 
    Customize: [required_in_a_row] can be changed to any number, 1 in a row will
      presumably end instantly
    
    :param player: integer represeting player
    :type player: int
    :param board: the master board (2d list) with integers as players
    :type board: list
    :param required_in_a_row: number of peices that are required to be in a row to win
    :type required_in_a_row: int

    :rtype: boolean
    :return: True for win found, False for no win found
    '''
    required_in_a_row: int = 4
    # itterate over every space over the board
    for i in range(len(board)):
        for j in range(len(board[i])):
            # pass coards to respective functions
            # NOTE: They all return boolean 
            if board[i][j] == 0:
                pass
            # if a forward (horizontal) win was found 
            if forward_check(i,j,player,board,required_in_a_row):
                return True
            if virtical_check(i,j,player,board,required_in_a_row):
                return True
            if to_right_diagonal_check(i,j,player,board,required_in_a_row):
                return True
            if to_left_diagonal_check(i,j,player,board,required_in_a_row):
                return True
            



    # after going through all the cords and a win was not found
    return False


def game() -> None:
### CONFIGURATION VARIALBES ###
    # Number of players. (MAX 6) 
    n_players = 2
    # Height of board
    height = 6
    # Width of board
    width = 7
    # Number of peices in a row for it to be counted as a win
    required_in_a_row = 4

    #--------------------------
    board = create_board(width,height)
    game_over = False
    # Track the current player using integers represeting each player
    player = 1
    while not game_over:
        display_board(board)
        # This variable is in the list index form (min being zero)
        column = get_valid_move(board) 
        #Update the master board
        board = update_board(column,board,player)
        #Check for win 
        if check_for_win(player,board,required_in_a_row):
            game_over=True
        
        # Switch Players if game not won 
        if not game_over: 
            player = player % n_players+1

    color_key_ending = {
        0:" ",
        1:(colors.YELLOW + "●" + colors.END),
        2:(colors.RED + "●" + colors.END),
        3:(colors.GREEN + "●" + colors.END),
        4:(colors.BLUE + "●" + colors.END),
        5:(colors.PURPLE + "●" + colors.END),
        6:(colors.CYAN + "●" + colors.END)
    }
    display_board(board)
    print(f"\nCONGRATULATIONS Player {player} {color_key_ending[player]} YOU WON!!! \n")
        



if __name__ == '__main__':
    game()
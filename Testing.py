def testing_creating_board_custom_demnsions():
    board = []
    for _ in range(10):
        row = []
        row.extend([0]*5)
        board.append(row)

    print(board)

def testing_check_for_win():
    def create_board(width, height):
        board = [[0,1,1,1,1,1,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0]]
        
        return board
    board = create_board(7,6)

    def forward_check(i,j,peice_num):
        '''
        This function will check for [required_in_a_row] in a row. 
        Customize: [required_in_a_row] can be changed to any number, 1 in a row will presumably end instantly
        
        :param i: the row (sublist) we are in on the board
        :type i: int
        :param j: the column (index) we are in on the row of the board
        :type j: int
        :param peice_num: the integeger representing the player on the master board 
        :type peice_num: int

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
        if j > len(board[i])-required_in_a_row:
            return False
        print(f"Current Peice: {peice_num}")
        # from the starting point check ahead [required_in_a_row] times
        for _ in range(required_in_a_row-1):
            print(f'{_+1}st Run')
            # check that the next checking possiion is within bounds
            if j + move_forward_count < len(board[i]):
                print(f'{j}+{move_forward_count} < {len(board[i])}, WITHIN BOUNDS')
                # if the peice to the right (however many right) is the same as the to be checked peice then add to [peice_in_a_row] counter
                if board[i][j+move_forward_count] == peice_num:
                    print(f'{board[i][j+move_forward_count]} == {peice_num}')
                    peice_in_row_count += 1
                    print(f"peice in row increased to: {peice_in_row_count}")
                    # if there were [required_in_a_row] in a row then call a win 
                    if peice_in_row_count >= required_in_a_row:
                        print(f'Returning Win: there were {peice_in_row_count} in a row')
                        # a return of true means there where 4 peices in a row 
                        return True
                # Cut this function short by return false (lose) after there wasnt another in a row, because if we are only checking [required_in_a_row] times then all of those times have to be true for it to be a win                 
                else:
                    return False
                move_forward_count += 1
            

    # go over each item and check if the left to right is a win 
    # for i in range(len(board)):
    for j in range(len(board[0])):
        # The peice that is in this spots checkings
        peice_num = board[0][j]
        win = forward_check(0,j,peice_num)
        print(win)
        print('----')
    
def testing_player_keep_track():
    n_turns = 5
    player = 1
    n_players = 2
    for i in range(n_turns):
        print(f'currently player {player}')
        # NOTE: DO STUFF 
        player = player % n_players+1


def testing_update_board():
    def create_board(width, height):
        board = [[0,1,1,1,1,1,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0]]
        
        return board
    class colors:
        RED = '\033[91m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        BLUE = '\033[94m'
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        WHITE = '\033[97m'
        END = '\033[0m'
    def display_board(board):
        color_key = {
            0:" ",
            1:(colors.YELLOW + "●" + colors.END),
            2:(colors.RED + "●" + colors.END),
            3:(colors.GREEN + "●" + colors.END),
            4:(colors.BLUE + "●" + colors.END),
            5:(colors.PURPLE + "●" + colors.END),
            6:(colors.CYAN + "●" + colors.END)
        }
        # NOTE: Color Key keys can only be values in the board that are values in the
        #  color key or else error 
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

    board = create_board(7,6)
    def update_board(): 
        column = int(input("Column: "))
        for i in range(len(board)-1,-1,-1):
            if board[i][column] == 0:
                up = i
                board[up][column] = 1
                display_board(board)
                break
    for _ in range(10):
        update_board()

testing_update_board()
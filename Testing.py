def testing_creating_board_custom_demnsions():
    board = []
    for _ in range(10):
        row = []
        row.extend([0]*5)
        board.append(row)

    print(board)
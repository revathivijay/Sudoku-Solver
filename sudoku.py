import numpy as np

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None

def convert(game):
    game = game.strip().split("\n")
    board = []
    for i in game:
        t = i.replace(' ', '').strip()
        t = list(t)
        t = list(map(int, t))
        board.append(t)
    return np.array(board)

def main():
    game = '''
              0 0 4 8 6 5 1 3 0
              0 6 1 0 0 4 5 9 0
              8 0 5 0 0 9 0 6 4
              5 4 3 2 0 6 0 0 1
              6 2 7 0 0 1 0 0 0
              0 0 8 0 4 3 0 0 6
              4 5 2 0 0 0 6 0 0 
              0 0 9 6 0 0 4 0 0
              0 0 6 4 0 0 0 1 5
          '''
    board = convert(game)

    if solve(board):
        print_board(board)
    else:
        print("loser!")

if __name__=='__main__':
    main()
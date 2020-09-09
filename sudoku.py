#Steps
#1 create board
#2 find first 0 square from left to right then down done
#3 check available numbers for that square
#4 insert first number in square
#5 repeat #2 | if doesnt work, insert next number|
#if no numbers left, go back to previous square

board = [[1, 0, 0, 0, 8, 4, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [4, 0, 0, 7, 0, 0, 0, 8, 0],
        [3, 0, 0, 4, 0, 0, 0, 6, 0],
        [5, 0, 1, 0, 2, 8, 0, 7, 3],
        [0, 0, 0, 6, 0, 0, 0, 0, 5],
        [0, 0, 7, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 5, 4, 0, 0, 0, 8]]


row_and_column = [0, 0]
def try_to_find_zero(row_and_column):
    for i in range(0,9):
        for j in range(0,9):
            if(board[i][j]==0):
                row_and_column[0] = i
                row_and_column[1] = j
                return True
    return False


def is_num_in_row(row, num):
    for i in range(0,9):
        if(board[row][i] == num):
            return True
    return False



def is_num_in_col(col, num):
    for i in range(0,9):
        if(board[i][col] == num):
            return True
    return False

def is_num_in_square(row, col, num):
    if (row <3):
         a = 0
         b = 3
    elif (row <6):
         a = 3
         b = 6
    else:
        a = 6
        b = 9
    if (col <3):
         c = 0
         d = 3
    elif (col <6):
         c = 3
         d = 6
    else:
        c = 6
        d = 9
    for i in range(a,b):
        for j in range(c,d):
            if(board[i][j] == num):
                return True
    return False


def is_num_available(row, col, num):
    return not is_num_in_row(row, num) and not is_num_in_col(col, num) and not is_num_in_square(row, col, num)


def try_first():
    if (not try_to_find_zero(row_and_column)):
        return True
    try_to_find_zero(row_and_column)
    row = row_and_column[0]
    col = row_and_column[1]

    for i in range(1,10):
        if(is_num_available(row, col, i)):
            board[row][col] = i
            if(try_first()):
                return True
            board[row][col] = 0
    return False

try_first()
print(board)

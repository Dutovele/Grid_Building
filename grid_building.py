
grid_rows = 0
grid_columns = 0
num_commands = 0
matrix = []
occupied = 0
commands = []
square_container = []

class square:
    def __init__(self, id, size, start_row, start_column):
        self.id = id
        self.size = size
        self.starting_co = [start_row, start_column]


def get_inputs():
    global grid_rows
    global grid_columns
    global num_commands
    global matrix
    global commands

    grid_rows, grid_columns, num_commands = input().split()
    grid_rows = int(grid_rows)
    grid_columns = int(grid_columns)
    num_commands = int(num_commands)

    for row in range(grid_rows):
        temp_col = []
        for col in range(grid_columns):
            temp_col.append(-1)

        matrix.append(temp_col)

    for cmd in range(num_commands):
        commands.append(input().split())


def matrix_print():
    global matrix
    global grid_rows
    global grid_columns

    for row in range(grid_rows):
        print(matrix[row])


def size_check(row_cor, col_cor, size):
    for row in range(size):
        for column in range(size):
            if (row + row_cor) > len(matrix) - 1 or (column + col_cor) > len(matrix[row]) - 1:
                return False
    return True


def put(row_cor, col_cor, size):
    global matrix
    global occupied
    global square_container


    if check(row_cor, col_cor, size) and size_check(row_cor, col_cor, size):

        temp_square = square(len(square_container), size, row_cor, col_cor)
        square_container.append(temp_square)

        for row in range(size):
            for column in range(size):
                matrix[row + row_cor][column + col_cor] = temp_square.id
        occupied = occupied+(size*size)


def put_existing(row_cor, col_cor, size,id):
    global matrix
    global occupied
    if size_check(row_cor, col_cor, size):
        for row in range(size):
            for column in range(size):
                matrix[row + row_cor][column + col_cor] = id
        occupied = occupied + (size * size)


def delete(row_cor, col_cor, size):
    global matrix
    global occupied
    global square_container


    for row in range(size):
        for column in range(size):
            matrix[row + row_cor][column + col_cor] = -1
    occupied = occupied - (size * size)


def move(row_cor, col_cor, direc):

    global matrix
    global square_container

    square_id = matrix[row_cor][col_cor]
    starting_cor = square_container[square_id].starting_co
    square_size = square_container[square_id].size

    if not check_empty(row_cor, col_cor):
        if direc == 'S':
            delete(starting_cor[0], starting_cor[1], square_size)
            if check(starting_cor[0]+1,starting_cor[1],square_size) and new_coordinate_check(starting_cor[0]+1,starting_cor[1]):
                put_existing(starting_cor[0]+1,starting_cor[1],square_size,square_id)
                starting_cor[0] = starting_cor[0] + 1
            else:
                put_existing(starting_cor[0], starting_cor[1], square_size, square_id)
        elif direc == 'N':
            delete(starting_cor[0], starting_cor[1], square_size)
            if check(starting_cor[0] - 1, starting_cor[1], square_size) and new_coordinate_check(starting_cor[0]-1,starting_cor[1]):
                put_existing(starting_cor[0] - 1, starting_cor[1], square_size, square_id)
                starting_cor[0] = starting_cor[0] - 1
            else:
                put_existing(starting_cor[0], starting_cor[1], square_size, square_id)
        elif direc == 'W':
            delete(starting_cor[0], starting_cor[1], square_size)
            if check(starting_cor[0], starting_cor[1] -1, square_size) and new_coordinate_check(starting_cor[0],starting_cor[1]-1):
                put_existing(starting_cor[0], starting_cor[1] -1, square_size, square_id)
                starting_cor[1] = starting_cor[1] - 1
            else:
                put_existing(starting_cor[0], starting_cor[1], square_size, square_id)
        elif direc == 'E':
            delete(starting_cor[0], starting_cor[1], square_size)
            if check(starting_cor[0], starting_cor[1] + 1, square_size) and new_coordinate_check(starting_cor[0],starting_cor[1]+1):
                put_existing(starting_cor[0], starting_cor[1] + 1, square_size, square_id)
                starting_cor[1] = starting_cor[1] + 1
            else:
                put_existing(starting_cor[0], starting_cor[1], square_size, square_id)


def new_coordinate_check(row,col):
    global grid_rows
    global grid_columns
    if row < 0 or row > grid_rows-1:
        return False
    if col < 0 or col > grid_columns-1:
        return False
    return True


def check(row_cor, col_cor, size):
    global matrix
    global occupied
    if size_check(row_cor, col_cor, size):
        for row in range(size):
            for column in range(size):
                if matrix[row + row_cor][column + col_cor] != -1:
                    return False
        return True

def check_empty(row_cor,col_cor):
    global matrix

    if(matrix[row_cor][col_cor] == -1):
        return True
    else:
        return False


def command_iterator():
    global matrix
    global occupied
    global square_container
    global number_of_squares
    global commands

    for cmd in commands:
        if cmd[0] == 'P':
            put(int(cmd[1]), int(cmd[2]), int(cmd[3]))
        elif cmd[0] == 'M':
            if len(square_container)>0:
                move(int(cmd[1]), int(cmd[2]), cmd[3])


def get_unoccupied_cells():
    global grid_columns
    global grid_rows
    global occupied
    area = grid_columns*grid_rows
    return area - occupied



get_inputs()
command_iterator()
print(get_unoccupied_cells())






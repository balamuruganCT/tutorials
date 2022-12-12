import queue


def ms2(field, row, col, row_i, col_i):
    toCheck = queue.Queue()
    if field[row_i][col_i] == 0:
        field[row_i][col_i] = -2
        toCheck.put((row_i, col_i))
    else:
        return field

    while not toCheck.empty():
        (curr_i, curr_j) = toCheck.get()
        for i in range(curr_i - 1, curr_i + 2):
            for j in range(curr_j - 1, curr_j + 2):
                if 0 <= curr_i < row and 0 <= curr_j < col and field[i][j] == 0:
                    field[i][j] = -2
                    toCheck.put((i, j))
    return field


if __name__ == "__main__":
    arr = [[0, 0, 0, 0, 0],
           [0, 1, 1, 1, 0],
           [0, 1, -1, 1, 0]]

    rows = 3
    cols = 5
    print(ms2(arr, rows, cols, 0, 1))

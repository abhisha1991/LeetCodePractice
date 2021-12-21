# https://codefights.com/interview-practice/task/SKZ45AF99NpbnvgTn/description
import numpy as np

def sudoku2(grid):
    size = 9
    rows = len(grid)
    flat_grid = np.array(grid).flatten()
    rowcount = 0
    for sg in grid:
        sg_numbers = [s for s in sg if s != '.']
        if len(sg_numbers) == 0:
            rowcount = rowcount + 1
            continue
        if len(sg_numbers) != len(set(sg_numbers)):
            return False
        i = 0
        for ele in sg:
            i = i + 1
            if ele is '.':
                continue
            for r in range(rows):
                idx = r*size + i
                if ele == flat_grid[idx-1] and r != rowcount:
                    return False
        rowcount = rowcount + 1
    return True


sudoku2([   [".",".","5",".",".",".",".",".","."],
            [".",".",".","8",".",".",".","3","."],
            [".","5",".",".","2",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","9"],
            [".",".",".",".",".",".","4",".","."],
            [".",".",".",".",".",".",".",".","7"],
            [".","1",".",".",".",".",".",".","."],
            ["2","4",".",".",".",".","9",".","."]])

sudoku2([['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']])
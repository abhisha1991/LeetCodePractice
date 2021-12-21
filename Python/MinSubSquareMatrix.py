# https://www.youtube.com/watch?v=_Lf1looyJMU


def min_sub_square_matrix(arr):
    lenarr = len(arr[0])
    mssm = [[0] * lenarr for x in range(lenarr)]
    maxi = 0
    for i in range(lenarr):
        for j in range(lenarr):
            if arr[i][j] == 1:
                # min of the top, left and top left elements + 1
                mssm[i][j] = 1 + min(mssm[i-1][j], mssm[i-1][j-1], mssm[i][j-1])
                if mssm[i][j] > maxi:
                    maxi = mssm[i][j]
    print(maxi)
    print(mssm)
    return maxi


min_sub_square_matrix([[0, 1, 1],  [0, 1, 1], [0, 1, 1]])
min_sub_square_matrix([[1, 1, 1],  [1, 1, 1], [1, 1, 1]])
min_sub_square_matrix([[0, 0, 0],  [1, 1, 1], [1, 1, 1]])
min_sub_square_matrix([[0, 0, 0],  [1, 0, 1], [1, 1, 0]])


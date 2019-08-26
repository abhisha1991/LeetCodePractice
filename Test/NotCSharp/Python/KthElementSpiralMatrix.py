# taken from 5.18 variant section of EPI
# adapted from here: https://www.geeksforgeeks.org/print-kth-element-spiral-form-matrix/
import numpy as np
def kthElementSpiral(mat, row, col, k):
    '''
    idea is that 
    if k <= col, then element is in the top edge
    if k <= col + row -1, then element is in right edge (why -1, because the top right edge is counted twice)
    if k <= col + row -1 + col -1, then element is in bottom edge
    if k <= col + row -1 + col -1 + row - 2, then element is in left edge (why -2? because top left and bottom left elements are already counted)
    if k is still larger, then move to the inner ring of the matrix and evaluate k - (col + row -1 + col -1 + row - 2) as the new k for the above conditions
    '''
    mat = np.array(mat)
    if row < 1 or col < 1:
        return "Not found"
    # case 1
    if k <= col:
        return mat[0][k-1] #top edge for x, ie, 0, and k-1 because we are looking for k-1 index
    # case 2
    if k <= col + row -1:
        return mat[k-col][col-1] # right edge for y, ie, col-1 and k-col because k > col (else case 1 would happen)
    # case 3
    if k <= col + row -1 + col -1:
        return mat[row-1][col-1-(k-(col+row-1))] # bottom edge for x, ie, row-1, for y axis, k > col+row-1, else case 2 would happen
    # case 4
    if k <= col + row -1 + col -1 + row -2:
        return mat[row-1-(k-(col+row-1+col-1))][0] # left edge for y axis, ie, 0, for x axis, k > col+row-1+col-1, else case 3 would happen
    
    mat = np.delete(mat, row-1, 0) # delete last row of mat
    mat = np.delete(mat, col-1, 1) # delete last column of mat
    mat = np.delete(mat, 0, 0) # delete first row of mat
    mat = np.delete(mat, 0, 1) # delete first column of mat
    
    return kthElementSpiral(mat, row-2, col-2, k-(col + row -1 + col -1 + row -2))

x = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(kthElementSpiral(x, 4, 4, 6))
x =  [[1, 2, 3, 4, 5, 6],[7, 8, 9, 10, 11, 12],[13, 14, 15, 16, 17, 18]]
print(kthElementSpiral(x, 3, 6, 17))

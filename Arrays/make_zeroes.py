'''
    Given a matrix of size n x m. make Zeroes, means in whole matrix when you find a zero, 
    convert its upper, lower, left, and right value to zero and 
    make that element the sum of the upper, lower, left and right value. 
    Do the following tasks according to the initial matrix
    (GFG)
'''
import copy

'''
    intuition:
    - Create a deep copy of the original matrix to keep track of the initial state.
    - Iterate to identify elements that are 0. For each zero found, sum up the values of its immediate neighbors (top, bottom, left, right) & update the current cell in the original matrix with this sum
    - Simultaneously, set the neighbors to 0
    - make sure to handle boundary conditions to avoid accessing out-of-bounds indices
'''
def solution(matrix: list[list[int]]):
    n = len(matrix)
    m = len(matrix[0])

    temp = copy.deepcopy(matrix)
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                if i + 1 < n:
                    matrix[i][j] += temp[i+1][j]
                    matrix[i+1][j] = 0
                if i - 1 >= 0:
                    matrix[i][j] += temp[i-1][j]
                    matrix[i-1][j] = 0
                if j + 1 < m:
                    matrix[i][j] += temp[i][j+1]
                    matrix[i][j+1] = 0
                if j - 1 >= 0:
                    matrix[i][j] += temp[i][j-1]
                    matrix[i][j-1] = 0

    return



if __name__ == '__main__':
    mymatrix = [[1, 2, 3, 4],
                [5, 6, 0, 7], 
                [8, 9, 4, 6],
                [8, 4, 5, 2]]
    # expected o/p = [[1, 2, 0, 4],[5, 0, 20, 0], [8, 9, 0, 6],[8, 4, 5, 2]]
    solution(mymatrix)
    print(mymatrix)

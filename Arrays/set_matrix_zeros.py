'''
    Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
    You must do it in place.
    (LC-73)
'''

def solution(arr: list[list[int]]):
    m = len(arr)
    n = len(arr[0])

    # row[i][...]
    # col[...][j]
    col0 = 1
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                arr[i][0] = 0
                if j != 0:
                    arr[0][j] = 0 
                else:
                    col0 = 0


    for i in range(1, m):
        for j in range(1, n):
            if arr[i][j] != 0:
                if arr[i][0] == 0 or arr[0][j] == 0:
                    arr[i][j] = 0
    

    if arr[0][0] == 0:
        for j in range(n):
            arr[0][j] = 0

    if col0 == 0:
        for i in range(n):
            arr[i][0] = 0
    
    return


if __name__ == '__main__':
    matrix = [[1,1,1], [1,0,1], [1,1,1]]
    # expected o/p = [[1,0,1], [0,0,0], [1,0,1]]
    solution(matrix)
    print(matrix)
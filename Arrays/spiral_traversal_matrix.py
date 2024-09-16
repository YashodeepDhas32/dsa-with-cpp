'''
    Given an m x n matrix, return all elements of the matrix in spiral order.
    LC-54
'''

'''
    intuition:
    - initialize left, right, top, bottom to keep track of edges in matrix and result to store numbers
    - run while loop untill top <= bottom and left <= right
    - 1st move = left to right, 2nd move = top to bottom, 3rd move = right to left, 4th move = bottom to top
    - repeat until boundaries cross
'''
def solution(matrix: list[list[int]]) -> list[int]:
    result = []
    m, n = len(matrix), len(matrix[0])
    left, right, top, bottom = 0, n - 1, 0, m - 1

    while(top <= bottom and left <= right):
        for i in range(left, right+1):
            result.append(matrix[top][i])
        top += 1
        for i in range(top, bottom+1):
            result.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left-1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


if __name__ == '__main__':
    mat = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    print(solution(mat))

    

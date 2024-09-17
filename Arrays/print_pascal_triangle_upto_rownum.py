'''
    Given an integer numRows, return the first numRows of Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
    (LC-118)
'''

def solution(numRows):
    result = []
    for k in range(1, numRows+1):
        ans = 1
        temp = []
        temp.append(1)
        
        for i in range(1, k):
            ans = ans * (k - i)
            ans = ans // i
            temp.append(ans)
        
        result.append(temp)

    return result

if __name__ == '__main__':

    numRows = 5
    # expected o/p = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]] 
    print(solution(numRows))
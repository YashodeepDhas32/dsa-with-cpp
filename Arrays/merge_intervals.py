'''
    Given an array of intervals where intervals[i] = [starti, endi], 
    merge all overlapping intervals, and return an array of the non-overlapping intervals 
    that cover all the intervals in the input.
    (LC - 56)
'''

'''
    intuition:
    - initialize empty result array of arrays and sort the intervals array to keep order
    - iterate over intervals array and check if result is empty or
    - check if 0th element of current ith array is greater than 1st element of recently added array into result, if yes then append current as new part of result
    - else, reassign the 1st element of recently added array between max of 1st element of recently added array and 1st element of current ith array 
'''
def solution(arr: list[list[int]]) -> list[list[int]]:
    result = []
    
    arr.sort()
    for i in range(len(arr)):
        if len(result) == 0 or arr[i][0] > result[-1][1]:
            result.append(arr[i])
        else:
            result[-1][1] = max(result[-1][1], arr[i][1])

    return result

if __name__ == "__main__":
    # 1, 6
    intervals = [[2, 4], [2, 6], [1, 3], [8, 9], [9, 11], [8, 10], [15, 18], [16, 17]]
    # expected op = [[1, 6], [8, 11], [15, 18]]
    print(solution(intervals))
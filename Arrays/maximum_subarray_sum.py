'''
    Given an integer array nums, find the subarray
    with the largest sum, and return its sum. (LC-53)
'''
import sys


'''
    intuition (uses kadane's algorithm):
    - keep max sum as smallest int and current sum as 0
    - run loop till end of array, keep adding every element with currentsum until currentsum is not negative
    - if currentsum is negative reassign it as 0 
    - if at any point currentsum is greater than maxsum, assign currentsum to maxsum
'''
def solution(arr):
    max_sum, current_sum = -sys.maxsize-1, 0
    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum

        if current_sum < 0:
            current_sum = 0

    return max_sum

if __name__ == '__main__':
    
    my_list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # expected o/p = 6 i.e [4,-1,2,1]
    print(f"maximum sum is = {solution(my_list)}")
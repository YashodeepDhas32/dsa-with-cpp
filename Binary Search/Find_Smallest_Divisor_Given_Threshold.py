'''
    Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, 
    divide all the array by it, and sum the division's result. Find the smallest divisor such that 
    the result mentioned above is less than or equal to threshold.
    Each result of the division is rounded to the nearest integer greater than or equal to that element. 
    (For example: 7/3 = 3 and 10/2 = 5).    
    (LC-1283)
'''
import math
def find_sum(arr, divisor):
    sum = 0
    for i in arr:
        sum += math.ceil(i / divisor)
    return sum

'''
    intution:
    - find the range, thats important, so here it starts from 1 to max in array(why?- bc if we consider all nums in array, after max number the ceil division result are same)
    - run binary search from low to high, calculate the mid, check if sum we get is less than equals threshold
    - to find the sum, we loop through array, keep adding the value of ith element / divisor to sum
    - since we need minimum divisor(mid) we keep trimming right half by lowering high, else incrementing low if condition does not satisfy
    - finally return the answer - minimum divisor
'''
def solution(arr, thresh):
    low, high = 1, float('-inf')
    for n in arr:
        high = max(n, high)
    
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if find_sum(arr, mid) <= thresh:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

if __name__ == "__main__":
    nums = [1, 2, 5, 9]
    threshold = 6
    print(solution(nums, threshold))
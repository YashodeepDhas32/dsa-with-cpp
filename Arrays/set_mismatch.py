'''
    You have a set of integers s, which originally contains all the numbers from 1 to n. 
    Unfortunately, due to some error, one of the numbers in s got duplicated to another number 
    in the set, which results in repetition of one number and loss of another number.
    Find the number that occurs twice and the number that is missing and return them in the form of an array.
    (LC-645)
'''

'''
    intuition:
    - calculate sum and sum of squares for array, also calculate sum of 1st n natural numbers and its squares
    - compute difference between actual and expected sum and same for actual and expected sum of squares
    - set 2 equations diff2 / diff1 = x + y and diff1 = x-y
'''
def solution(nums):
    n = len(nums)
    # find sum of nums and squared sum of nums
    arrsum, sqsum = 0, 0
    for i in range(n):
        arrsum += nums[i]
        sqsum += (nums[i] * nums[i])

    # find sum of first n natrual nums and squared sum of same
    nsum = (n * (n + 1)) // 2
    nsqsum = (n * (n + 1) * ((2*n) + 1)) // 6

    diff1 = arrsum - nsum
    diff2 = sqsum - nsqsum
    diff2 = diff2 // diff1

    x = (diff1 + diff2) // 2
    y = x - diff1

    return [x, y]

if __name__ == "__main__":
    arr = [1, 2, 2, 4]
    # expected op = [2, 3]
    print(solution(arr))
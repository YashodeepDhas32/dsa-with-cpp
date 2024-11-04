'''
    Given an integer n, find the square root of n. If n is not a perfect square, 
    then return the floor value.
    (GFG)
'''
'''
    intuition:
    - using binary search, we search in pool of numbers from 1 to Num, calculate the mid
    - check if mid*mid is less than or equal to num, then set ans as mid and keep increasing low
    - else decrease high, to find the square/perfect square of mid as the Num
'''
def solution(num):
    ans = -1
    low, high = 1, n
    while low <= high:
        mid = (low + high) // 2
        if (mid * mid) <= num:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1 
    return ans


if __name__ == "__main__":
    n = 5
    # expected op = 2
    print(solution(n))
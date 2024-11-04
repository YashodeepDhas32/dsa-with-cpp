'''
    Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
    The guards have gone and will come back in h hours.
    Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas 
    and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead 
    and will not eat any more bananas during this hour.
    Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
    Return the minimum integer k such that she can eat all the bananas within h hours.
    (LC-875)
'''
import math, sys
def findTotalHours(piles, mid):
    total = 0
    for n in piles:
        total += math.ceil(n / mid)

    return total

'''
    intuition:
    - find the max value in piles array, and set it as high and set low as 1
    - run binary search algo, calculate mid, then write a function to calculate total hours
    - return summation of total with ceilin value of (piles[i] / mid) as total hours
    - check if totalHours less than equals "h" hours, if yes then mark mid as k and keep eliminating right half
    - why ? - because we want minimum integer k so we will find it at left half until it satisfies condition, 
    - else trim down left half, finally return the k
'''
def solution(piles: list[int], h: int) -> int:
    mx = -sys.maxsize-1
    for n in piles:
        mx = max(mx, n)
    
    k = -1
    low, high = 1, mx
    while low <= high:
        mid = (low + high) // 2
        totalHours = findTotalHours(piles, mid)
        if totalHours <= h:
            k = mid
            high = mid - 1
        else:
            low = mid + 1

    return k

if __name__ == "__main__":
    piles = [3, 6, 7, 11]
    h = 8
    print(solution(piles, h))
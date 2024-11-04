'''
    You are given an integer array bloomDay, an integer m and an integer k.
    You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
    The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
    Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1
    (LC-1482)
'''

def possible(bloomDay, mid, m, k):
    ans = 0
    count = 0
    for i in range(len(bloomDay)):
        if bloomDay[i] <= mid:
            count += 1
        else:
            ans += count // k
            count = 0
    ans += count // k
    return ans >= m

'''
    intuition:
    - check a case where bouquets multiplied by adjacents exceed length of array, then return -1
    - else find the range, find min and max element in array, traverse between that range for binary search
    - calculate mid, check if making bouquets is possible, by passing mid to possible()
    - we check for every ith element if its <= mid, then increment count
    - else, we append ans with count/k and revert count to 0, since we need adjacent flowers only,
    - finally we return the boolean we get by comaring ans >= total required bouquets
    - we keep trimming high, since we want minimum answer possible
'''
def solution(bloomDay: list[int], m: int, k: int):
    if m * k > len(bloomDay): 
        return -1
    
    low, high = float('inf'), float('-inf')
    for i in range(len(bloomDay)):
        low = min(low, bloomDay[i])
        high = max(high, bloomDay[i])
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if possible(bloomDay, mid, m, k):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans

if __name__ == "__main__":
    bloomDay = [1,10,3,10,2]
    m = 3
    k = 1
    # expected op = 3
    print(solution(bloomDay, m, k))
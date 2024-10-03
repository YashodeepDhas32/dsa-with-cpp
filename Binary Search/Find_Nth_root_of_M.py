'''
    You are given 2 numbers (n , m); the task is to find n√m (nth root of m)
    (GFG)
'''

'''
    intuition:
    - just a bineary search approach, caculate run loop till low <= high and calculate mid
    - we need to find (mid power of N) equalling M
    - if mid power of N is less than M then increment low
    - else mid power of N is greater than M decrement high
'''
def solution(N, M):
    ans = -1
    low, high = 1, M
    while low <= high:
        mid = (low + high) // 2
        if mid ** N == M:
            ans = mid
            return ans
        elif mid ** N < M:
            low = mid + 1
        else:
            high = mid - 1

    return ans

if __name__ == "__main__":
    n = 2, m = 3
    print(solution(n, m))
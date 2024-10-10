'''
    A conveyor belt has packages that must be shipped from one port to another within days days.
    The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship 
    with packages on the conveyor belt (in the order given by weights). We may not load more weight
    than the maximum weight capacity of the ship. Return the least weight capacity of the ship that
    will result in all the packages on the conveyor belt being shipped within days days.
    (LC-1011)
'''
def findDays(weights, capacity):
    load, days = 0, 1
    for w in weights:
        if w + load > capacity:
            days += 1
            load = w
        else:
            load += w
    return days
'''
    intuition:
    - most important:identify the range, to ship all the weights we need to have max weight in array as low
    - and high can be sum of all weights in array, so answer would lie between this range
    - then run basic binary search, calculate the mid, write a find days function, where we set days=1
    - we run a loop to check if sum of wth weight and current load exceeds(>) capacity, increment days by 1 and assign load to wth weight
    - if sum does not exceed capacity, we keep on summing up load with weights in array, then return the days
    - check if days are <= given days, assign mid to answer and keep trimming right half of range since we want least weight(mid) capacity
    - else trim the left half of array, finally return the answer
'''
def solution(weights, given_days):
    low, high = float('-inf'), 0
    for w in weights:
        low = max(low, w)
        high += w
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if findDays(weights, mid) <= given_days:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

if __name__ == "__main__":
    weights = [1,2,3,4,5,6,7,8,9,10]
    days = 5
    print(solution(weights, days))
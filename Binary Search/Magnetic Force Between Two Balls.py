'''
    In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls 
    if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at 
    position[i], Morty has m balls and needs to distribute the balls into the baskets such that 
    the minimum magnetic force between any two balls is maximum.
    Rick stated that magnetic force between two different balls at positions x and y is |x - y|.
    Given the integer array position and the integer m. Return the required force.
    (LC-1552)
'''
def isFeasible(position, m, distance):
    count_of_balls = 1
    last_ball = position[0]
    for i in range(1, len(position)):
        if position[i] - last_ball >= distance:
            count_of_balls += 1
            last_ball = position[i]
    
    return True if count_of_balls >= m else False
'''
    intuition (exactly same as aggressive cows):
    - we sort the initial positions array, to apply binary search, initialize low as 1 and high as array[max]-array[min] 
    - so our answer lies between low and high range, we run a binary search and calculate mid
    - we then set mid as distance, for isFeasible function where, we keep count of balls as 1 initially,
    - and last ball as 1st item in position array, then we run a loop from 1st index to last of array
    - check if difference of ith ball and last ball is >= distance, if yes then increment count of balls and assign ith ball as last ball
    - finally we return True if count of balls is >= m balls else return False
    - if our feasible function returns true we assign asnwer as mid, and try to find maximum distance, by eliminating left half of array
    - if function return false we eliminate right half
'''
def solution(position, m):
    position.sort()
    low, high = 1, position[len(position)-1] - position[0]
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if isFeasible(position, m, mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
        
    return ans

if __name__ == "__main__":
    position = [1, 2, 3, 4, 7]
    m = 3
    # expected op = 3
    print(solution(position, m))
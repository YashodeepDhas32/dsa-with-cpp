'''
    Given a sorted array of distinct integers and a target value, return the index 
    if the target is found. If not, return the index where it would be if it were inserted in order.
    (LC-35)
'''

'''
    intuition:
    - based on binary search do the process, also store initial ans as len of array if target is greater than max in array
    - if arr[mid] >= target store the ans as mid
    - return ans
'''
def solution(arr, target):
    n = len(arr)
    ans = n
    low, high = 0, n-1

    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 2
    # expected o/p = 1 (2 should be placed at 1st index)
    print(solution(nums, target))
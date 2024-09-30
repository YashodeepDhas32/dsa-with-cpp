'''
    Given an array of integers nums which is sorted in ascending order, 
    and an integer target, write a function to search target in nums. 
    If target exists, then return its index. Otherwise, return -1.
    LC-704
'''

'''
    intuition: binary search algo
    - set low as 0th index and high as last index
    - run while low less than equals high and calculate mid of array (for integer overflow do - (low + (high-low))// 2)
    - check if current midth element matches target if yes return midth index
    - else if current midth element is greater then reduce high to mid - 1
    - else increase low to mid + 1
    - can be done iteratively as well 
'''
def solution(arr, n, target):
    low, high = 0, n-1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    # expected op = 4
    print(solution(nums, len(nums), 9))
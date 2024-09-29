'''
    There is an integer array nums sorted in ascending order (with distinct values).
    Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k 
    (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0],
    nums[1], ..., nums[k-1]] (0-indexed). 
    (LC-33)
'''

'''
    intuition:
    - if mid matches target return the mid, else do below steps
    - check if left half of array is sorted by comparing array of low with mid, if yes then
    - check if target lies between array of low and array of mid, if yes then trim right half by reducing high, else trim left half by increasing low
    - else(if fails), the right half of array might be sorted, then 
    - then check target lies between arr of mid and arr of high, then trim left half or else trim right half
    - finally mid is not found then return -1
'''
def solution(arr, target):
    low, high = 0, len(arr)-1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        else:
            # left half of array is sorted
            if arr[low] <= arr[mid]:
                # target lies between low and mid
                if arr[low] <= target and target <= arr[mid]:
                    # trim the right half
                    high = mid - 1
                # target does not lie in low and mid, trim right half
                else:
                    low = mid + 1
            # right half of array is sorted
            else:
                # target lies in right half
                if arr[mid] <= target and target <= arr[high]:
                    # trim left half
                    low = mid + 1
                else:
                    # trim right half
                    high = mid - 1


    return -1

if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    # expected output: index 4
    print(solution(nums, target))
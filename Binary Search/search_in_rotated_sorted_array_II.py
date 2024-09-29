'''
    There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
    rest is same as LC-33
    (LC-81)
'''
'''
    intuition:
    - do same stuff as searching in rotated sorted array, wiht unique elements
    - since here are duplicates we just need to add one check, whether
    - check arr of low equals arr of mid and arr of mid equals arr of high
    - if yes then keep trimming down left and right, by incrementing low and decrementing high
    - use continue to skip steps below this condition, since above check can happen multiple times
'''
def solution(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue
        if arr[low] <= arr[mid]:
            if arr[low] <= target and target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] <= target and target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
        
    return False

if __name__ == "__main__":
    nums = [3, 3, 1, 3, 3, 3, 3]
    target = 1
    # expected op = True
    print(solution(nums, target))
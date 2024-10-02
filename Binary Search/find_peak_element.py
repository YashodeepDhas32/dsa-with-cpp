'''
    A peak element is an element that is strictly greater than its neighbors.
    Given a 0-indexed integer array nums, find a peak element, and return its index. 
    If the array contains multiple peaks, return the index to any of the peaks.
    You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always 
    considered to be strictly greater than a neighbor that is outside the array.
    (LC-162)
'''

'''
    intuition:
    - check edge case: if n is 1 or first element is greater than second, (assume left as -infy) return index 0 as peak
    - check edge case: if last element is greater than second last element (assume right as -infy) return n-1 as peak
    - run basic binary search, calculate mid, check if mid element is greater than left and right adjacent elements, return mid
    - check if mid element is smaller than mid+1 element, meaning right side can contain peak, since range can be increasing order, till peak
    - then eliminate left half, else peak can be on left half, then eliminiate right half

'''
def solution(arr, n):
    if n==1 or arr[0] > arr[1]:
        return 0
    if arr[n-1] > arr[n-2]:
        return n-1
    
    low, high = 1, n-2
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
            return mid
        if arr[mid] < arr[mid+1]:
            low = mid + 1
        else:
            high = mid - 1

    return -1

if __name__ == "__main__":
    nums = [1, 2, 1, 3, 5, 6, 4]
    # expect output = index 5 (i.e number 6)
    print(solution(nums, len(nums)))


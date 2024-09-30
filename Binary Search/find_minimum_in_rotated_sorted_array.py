'''
    Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
    For example, the array nums = [0,1,2,4,5,6,7] might become:
    Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
    Given the sorted rotated array nums of unique elements, return the minimum element of this array.
    (LC-153)
'''
import sys
'''
    intuition:
    - run binary search algo, compute mid
    - check if array is already sorted, or at point if its sorted, then mark min between mini and arr[low] and break
    - check if left half of arr is sorted, then assign mini to min of mini and arr of low and eliminate right half
    - else right half must be sorted then, then assign mini to min of mini and arr of mid and elminate left half
    - return min
'''
def solution(arr):
    mini = sys.maxsize
    low, high = 0, len(arr)-1

    while low <= high:
        mid = (low + high) // 2
        # if arr is already sorted
        if arr[low] <= arr[high]:
            mini = min(mini, arr[low])
            break
        # check if left half is sorted and eliminate right half
        if arr[low] <= arr[mid]:
            mini = min(mini, arr[low])
            high = mid - 1
        else:
            mini = min(mini, arr[mid])
            low = mid + 1
        
    return mini


if __name__ == "__main__":
    nums = [4, 5, 1, 2, 3]
    # expected output = 1
    print(solution())
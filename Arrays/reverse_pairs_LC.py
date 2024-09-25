'''
    Given an integer array nums, return the number of reverse pairs in the array.
    A reverse pair is a pair (i, j) where:
    0 <= i < j < nums.length and
    nums[i] > 2 * nums[j].
    (LC-493)
'''

'''
    intuition: (using merge sort algorithm)
    - we will be comparing the left sorted array and right sorted array elements
    - run a loop to traverse from left sorted array (low to mid)
    - run a while loop until the current (i) element is 2x more than current right element
    - keep increment right until we find such elements
    - finally increment count by subtracting mid+1 from right i.e (right - (mid+1))
'''
def solution(arr, n):
    return merge_sort(arr, 0, n)

def merge(arr, low, mid, high):
    left = low
    right = mid + 1
    temp = []

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high+1):
        arr[i] = temp[i-low]

def reverse_pairs(arr, low, mid, high):
    right = mid + 1
    count = 0
    for i in range(low, mid + 1):
        while right <= high and arr[i] > 2*arr[right]:
            right += 1

        count += ( right - ( mid + 1 ))
    return count

def merge_sort(arr, low, high):
    count = 0
    if low >= high:
        return count
    mid = (low + high)//2
    count += merge_sort(arr, low, mid)
    count += merge_sort(arr, mid + 1, high)
    count += reverse_pairs(arr, low, mid, high)
    merge(arr, low, mid, high)
    return count 

    
if __name__ == '__main__':
    nums = [2, 4, 3, 5, 1]
    n = len(nums) - 1
    # expected o/p = 3 i.e reverse pairs = (1,4), (2,4), (3,4)
    print(solution(nums, n))
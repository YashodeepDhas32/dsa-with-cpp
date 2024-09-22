''' 
    Given two sorted arrays in non-decreasing order. Merge them in sorted order 
    without using any extra space. Modify arr1 so that it contains the first N elements 
    and modify arr2 so that it contains the last M elements.
    (GFG)
'''

'''
    intuition:
    - 
    - initialize i pointer for arr1 as n-1 and j pointer for arr2 as 0
    - run while loop till i greater than equal to 0 and j less than m
    - start to swap from last element of arr1 and first element of arr2, if last > first
    - else break since we got our elements in place and rest of arrays seem to be fine
    - finally sort both arrays to keep elements in sorted order
'''
def solution(arr1, arr2, n, m):
    i, j = n - 1, 0
    while i >= 0 and j < m:
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
        else:
            break

    arr1.sort()
    arr2.sort()
    
    # not expected just to show output 
    return arr1 + arr2

if __name__ == "__main__":
    nums1 = [1, 3, 2]
    nums2 = [8, 8, 4, 5]
    # expected op = [1, 2, 3, 4, 5, 8, 8]
    print(solution(nums1, nums2, len(nums1), len(nums2)))
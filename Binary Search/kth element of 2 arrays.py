'''
    Given two sorted arrays arr1 and arr2 and an element k. 
    The task is to find the element that would be at the kth position of the combined sorted array.
    (GFG)
'''

def solution(arr1: list[int], arr2: list[int], k: int):    
    n1, n2 = len(arr1), len(arr2)
    if n1 > n2 :
        return solution(arr2, arr1, k)
    
    low, high = max(0, k-n2), min(k, n1)
    left = k
    n = n1 + n2
    while low <= high:
        mid1 = (low + high) // 2
        mid2 = left - mid1
        l1, l2 = float('-inf'), float('-inf')
        r1, r2 = float('inf'), float('inf')
        if mid1 < n1:
            r1 = arr1[mid1]
        if mid2 < n2:
            r2 = arr2[mid2]
        if mid1 - 1 >= 0:
            l1 = arr1[mid1 - 1]
        if mid2 - 1 >=0:
            l2 = arr2[mid2 - 1]
        if l1 <= r2 and l2 <= r1:
            return max(l1 , l2)
        elif l1 > l2:
            high = mid1 - 1
        else:
            low = mid1 + 1

    return None

if __name__ == '__main__':
    nums1, nums2 = [2, 3, 6, 7, 9], [1, 4, 8, 10]
    k = 5
    
    # expected op = 6 (5th element after both arrays are merged in sorted order)
    print(solution(nums1, nums2, k))

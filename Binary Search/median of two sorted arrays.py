'''
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the 
    two sorted arrays. The overall run time complexity should be O(log (m+n)).
    (LC-4)
'''

def solution(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    if n1 > n2:
        return solution(nums2, nums1)
    
    low, high = 0, n1
    left = (n1 + n2 + 1) // 2
    n = n1 + n2    
    while low <= high:
        mid1 = (low + high) // 2
        mid2 = left - mid1
        l1, l2 = float('-inf'), float('-inf')
        r1, r2 = float('inf'), float('inf')
        if mid1 < n1:
            r1 = nums1[mid1]
        if mid2 < n2:
            r2 = nums2[mid2]
        if mid1 - 1 >= 0:
            l1 = nums1[mid1 - 1]
        if mid2 - 1 >= 0:
            l2 = nums2[mid2 - 1]
        if l1 <= r2 and l2 <= r1:
            if n % 2 == 1:
                return max(l1, l2)
            return float((max(l1, l2) + min(r1, r2)) / 2.0)
        elif l1 > l2:
            high = mid1 - 1
        else:
            low = mid1 + 1 




if __name__ == '__main__':
    nums1, nums2 = [1, 2], [3, 4]
    # expected op = 2.50000
    print(solution(nums1, nums2))
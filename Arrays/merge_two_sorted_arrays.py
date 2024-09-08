'''
    The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
    To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
    and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''


def solution(nums1, nums2, m, n):
    # last index of nums1
    last = (m + n) - 1
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1            
        last -= 1

    while n > 0:
        nums1[last] = nums2[n - 1]
        n -= 1
        last -= 1
    

    return nums1


if __name__ == '__main__':
    my_list1 = [1,2,3,0,0,0,0]
    my_list2 = [1,2,5,6]
    print(solution(my_list1, my_list2, 3, len(my_list2)))

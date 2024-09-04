'''
    LC - 349
    Given two integer arrays nums1 and nums2, return an array of their intersection
    Each element in the result must be unique and you may return the result in any order.
'''

def solution(nums1, nums2) -> list[int]:
    # set for storing unique elements from nums1
    unique_from_nums1 = set(nums1)

    result = []
    # check if item exist in set if yes add in result and remove from set
    for i in range(0, len(nums2)):
        if nums2[i] in unique_from_nums1:
            result.append(nums2[i])
            unique_from_nums1.discard(nums2[i])

    return result


if __name__ == '__main__':
    my_list1 = [4,9,5]
    my_list2 = [9,4,9,8,4]
    print(solution(my_list1, my_list2))
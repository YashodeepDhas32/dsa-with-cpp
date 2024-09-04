'''
    Given two sorted arrays arr1[] and arr2[]. Your task is to return the intersection of both arrays.
    Intersection of two arrays is said to be elements that are common in both arrays. 
    The intersection should not count duplicate elements.
    Note: If the intersection is empty then the list should contain -1.
    [GFG]
'''

def solution(arr1, arr2):
    result = []
    i, j = 0, 0

    while(i < len(arr1) and j < len(arr2)):
        if arr1[i] == arr2[j]:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return result if result else [-1]

if __name__ == '__main__':
    my_list1 = [1, 2, 2, 3, 4]
    my_list2 = [2, 2, 4, 6, 7, 8]
    # expected o/p = [2, 4]

    print(solution(my_list1, my_list2))
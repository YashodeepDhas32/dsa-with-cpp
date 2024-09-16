'''
    You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
    You should return the array of nums such that the the array follows the given conditions:
    - Every consecutive pair of integers have opposite signs.
    - For all integers with the same sign, the order in which they were present in nums is preserved.
    - The rearranged array begins with a positive integer.
    (LC - 2149)
'''

'''
    intuition:
    - populate result array with 0's initially and pos with 0 and neg with 1 since result begins with +ve int
    - traverse through array, if current element is positive add it to pos index of result and increment pos
    - if current element is neg add it to neg index of result and increment neg
'''
def solution(arr):
    result = [0] * len(arr)
    pos, neg = 0, 1
    for i in range(len(arr)):
        if arr[i] > 0:
            result[pos] = arr[i]
            pos += 2
        else:
            result[neg] = arr[i]
            neg += 2

    return result

if __name__ == '__main__':                  
    my_list = [3, 1, -2, -5, 2, -4]
    # expected o/p = [3, -2, 1, -5, 2, -4]
    print(f"Rearranged Array - {solution(my_list)}")
'''
    Given an integer array nums, find a subarray
    that has the largest product, and return the product.
    LC-152
'''
import sys

'''
    intuition:
    - a case to consider is product of any number with 0 is 0, so we need to avoid 0's here (if encountered)
    - so run a loop from start to end for given array, (we will be doing for prefix and suffix, so consider from back as well)
    - whenever 0's encountered reassign pref/suff back to 1 since no point in having that product
    - at end of every iteration check max of previous maxi and max of prefix and suffix multiplication
'''
def solution(arr, n):
    maxi = -sys.maxsize-1
    pref, suff = 1, 1
    for i in range(n):
        if pref == 0:
            pref = 1
        if suff == 0:
            suff = 1
        pref = pref * arr[i]
        suff = suff * arr[n - i - 1]

        maxi = max(maxi, max(pref, suff))

    return maxi

if __name__ == '__main__':
    nums = [6, -3, -10, 0, 2]
    print(solution(nums, len(nums)))
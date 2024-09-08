'''
    Given an array nums containing n distinct numbers in the range [0, n], 
    return the only number in the range that is missing from the array.
    LC-268
'''

def solution(nums, n) -> int:
    xor1, xor2 = 0, 0

    for i in range(0, n):
        xor1 = xor1 ^ (i+1)
        xor2 = xor2 ^ nums[i]

    return xor1 ^ xor2


if __name__ == '__main__':
    nums = [9,6,4,2,3,5,7,0,1]
    n = len(nums)
    # expected o/p -> 8
    print(solution(nums, n))
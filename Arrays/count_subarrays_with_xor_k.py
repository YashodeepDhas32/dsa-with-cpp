'''
    Given an array and an integer k, find the number of subarrays of array whose bitwise XOR
    of all elements is equal to k.
'''

'''
    intuition:
    - initialize dictionary with 0: 1 to handle case of subarray starting from beginning of array
    - keep adding prefix xor in xor and calculate XOR of xor and k and store in x
    - check if remaining x previously exists in map, if yes then increment count with frequency of x
    - check if prefix xor exists in map if yes then increment frequency of prefix xor in map, else assign it as 1
'''
def solution(arr, k):
    count = 0
    xor = 0
    mp = dict({0: 1})
    for i in range(len(arr)):
        xor = xor ^ arr[i]

        x = xor ^ k
        if x in mp:
            count += mp[x]
        
        if xor in mp:
            mp[xor] += 1
        else:
            mp[xor] = 1

    return count

if __name__ == "__main__":
    nums = [4, 2, 2, 6, 4]
    k = 6
    # expected o/p = 4 subarays - [4, 2], [2, 2, 6], [6], [4,2,2,6,4]
    print(solution(nums, k))
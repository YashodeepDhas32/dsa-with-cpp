'''
    You are given a 0-indexed integer array nums. In one operation, you can:
    Choose two different indices i and j such that 0 <= i, j < nums.length.
    Choose a non-negative integer k such that the kth bit (0-indexed) in the binary representation of nums[i] and nums[j] is 1.
    Subtract 2k from nums[i] and nums[j].
    A subarray is beautiful if it is possible to make all of its elements equal to 0 after applying the above operation any number of times.
    Return the number of beautiful subarrays in the array nums.
    (LC-2588)
'''

'''
    intuition:
    - The idea is to use the properties of the XOR operation and prefix XOR sums 
    to efficiently count the number of subarrays that can be made zero. By tracking 
    the occurrences of prefix XOR values, we can determine the number of beautiful 
    subarrays in linear time. This method leverages the insight that a subarray has an 
    XOR of zero if the prefix XOR at the end of the subarray equals the prefix XOR at the 
    start of the subarray.
'''
def solution(arr):
    count, prefix_xor = 0, 0
    mp = {0: 1}
    for i in range(len(arr)):
        prefix_xor = prefix_xor ^ arr[i]

        if prefix_xor in mp:
            count += mp[prefix_xor]
        
        if prefix_xor in mp:
            mp[prefix_xor] += 1
        else:
            mp[prefix_xor] = 1
    
    return count

if __name__ == '__main__':
    nums = [4,3,1,2,4]
    # expected op = 2
    print(solution(nums))
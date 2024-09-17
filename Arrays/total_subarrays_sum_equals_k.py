'''
    Given an array of integers and an integer k, 
    return the total number of subarrays whose sum equals to k.
    A subarray is a contiguous non-empty sequence of elements within an array.
    LC-560
'''

'''
    intuition:
    - initialize dictionary with 0: 1 to handle case of subarray starting from beginning of array
    - keep adding prefix sum in psum and calculate difference of prefix sum and k and store in rsum
    - check if remaining sum(rsum) previously exists in map, if yes then increment count with frequency of rsum
    - check if prefix sum exists in map if yes then increment frequency of prefix sum in map, else assign it as 1
'''
def solution(arr, k):
    mp, psum, count = dict({0: 1}), 0, 0

    for i in range(len(arr)):
        psum += arr[i]

        rsum = psum - k
        if rsum in mp:
            count += mp[rsum]

        if psum in mp:
            mp[psum] += 1
        else:
            mp[psum] = 1

    return count


if __name__ == '__main__':
    mylist = [10, 2, -2, -20, 10]
    k = -10
    # expected op = 3 (total 3 subarrays with sum k)
    print(solution(mylist, k))
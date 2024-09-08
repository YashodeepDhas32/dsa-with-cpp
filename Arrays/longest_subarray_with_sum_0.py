'''
    Given an array arr[] of size n, the task is to find the length of the longest subarray with sum equal to 0.
    [GFG] - (variation of longest sub array-with sum k)
'''


'''
    intuition:
    - Maintain running prefix sum to identify subarrays.
    - Use a dictionary to store the first occurrence of each prefix sum.
    - Check for target sum (here 0) by comparing prefix sum.
    - Store unique prefix sums to ensure the earliest occurrence.
'''
def solution(arr, n) -> int:
    max_len, prefix_sum, mp = 0, 0, dict()

    for i in range(0, n):
        prefix_sum += arr[i]

        if prefix_sum == 0:
            max_len = i + 1

        if prefix_sum in mp:
            max_len = max(max_len, i - mp[prefix_sum])
        else:
            mp[prefix_sum] = i

    return max_len


if __name__ == '__main__':
    arr = [15, -2, 2, -8, 1, 7, 10, 23]
    n = len(arr)
    # expected o/p - 5 i.e [-2, 2, -8, 1, 7]
    print(f'longest sub array with sum 0 is {solution(arr, n)}')

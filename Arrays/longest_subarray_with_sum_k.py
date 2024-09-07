'''
    Given an array containing integers and a value k. 
    find the length of the longest Sub-Array with the sum of the elements equal to the given value k. 
'''

def solution(arr, k):
    max_len, prefix_sum, mp = 0, 0, dict()

    for i in range(0, len(arr)):
        prefix_sum += arr[i]

        if prefix_sum == k:
            max_len = i + 1

        if prefix_sum - k in mp:
            max_len = max(max_len, i - mp[prefix_sum-k])

        if prefix_sum not in mp:
            mp[prefix_sum] = i

    return max_len


if __name__ == "__main__":

    my_list = [1, -1, 5, -2, 3]
    k = 3
    # expected o/p = 4 

    print(f'length of longest subarray - {solution(my_list, k)}')

'''
    Largest subarray of 0's and 1's (GFG)
    Given an array of 0s and 1s. Find the length of the largest subarray with equal number of 0s and 1s.
'''

'''
    intuition: (everything same as longest sub array-with sum 0 with added extras)
    - convert all 0's in array to -1's
    - initialize dictionary with {0:-1} to handle subarrays starting from index 0    
'''

def solution(arr, n):
    max_len, prefix_sum, mp = 0, 0, { 0: -1 }

    arr = [-1 if num == 0 else 1 for num in arr]

    for i in range(n):
        prefix_sum += arr[i]

        if prefix_sum in mp:
            max_len = max(max_len, i - mp[prefix_sum])
        else:
            mp[prefix_sum] = i
        
    return max_len


if __name__ == '__main__':
    my_list = [1, 0, 1, 1, 1, 0, 0]
    size = len(my_list)
    # expected o/p - 6 i.e -[0, 1, 1, 1, 0, 0]
    print(f"largest length subarray with 0's and 1's - {solution(my_list, size)}")
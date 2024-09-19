'''
    Given an integer array, return all the triplets [nums[i], nums[j], nums[k]] 
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    Notice that the solution set must not contain duplicate triplets
    (LC-15)
'''

'''
    intuition:
    - sort the array and run a loop till end of sorted array
    - skip the loop with continue if current ith element is same as previous ith element
    - else assign j as next of i and k as last and run while j is less than k
    - check if sum is less than zero then increment j, sum is greater then decrement k else assign ith, jth and kth element to result
    - increment i and decrement j and keep incrementing j till jth element is different than j-1th element 
    - keep decrementing k till kth element is different than k+1th element  
'''
def solution(arr: list) -> list[list[int]]:
    result = []
    n = len(arr)
    arr.sort()
    for i in range(n):
        if i > 0 and arr[i] == arr[i-1]:
            continue

        j = i + 1
        k = n - 1
        while j < k:
            total = arr[i] + arr[j] + arr[k]
            if total < 0:
                j += 1
            elif total > 0:
                k -= 1
            else:
                result.append([arr[i], arr[j], arr[k]])
                j += 1
                k -= 1
                while j < k and arr[j] == arr[j-1]:
                    j += 1
                while j < k and arr[k] == arr[k+1]:
                    k -= 1
    
    return result

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    # expected op = [[-1,0,1], [-1,-1,2]]
    print(solution(nums))
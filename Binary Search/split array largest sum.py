'''
    Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the 
    largest sum of any subarray is minimized. Return the minimized largest sum of the split.
    (LC-410)
'''

def find_splits(arr, N, mid):
    count_of_splits, total_split_sum = 1, 0
    for i in range(N):
        if arr[i] + total_split_sum <= mid:
            total_split_sum += arr[i]
        else:
            total_split_sum = arr[i]
            count_of_splits += 1
    
    return count_of_splits

'''
    intuition: - exactly same as book allocation problem
'''
def solution(arr, N, K):
    low, high = max(arr), sum(arr)
    while low <= high:
        mid = (low + high) // 2
        splits = find_splits(arr, N, mid)
        if splits <= K:
            high = mid - 1
        else:
            low = mid + 1
    return low

if __name__ == "__main__":
    nums = [7, 2, 5, 10, 8]
    k = 2
    # expected op = 18 i.e (7+2+5)=14 and (10+8)=18 largest sum among the two subarrays is minimum 18
    print(solution(nums, len(nums), k))
'''
    Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
    Return the kth positive integer that is missing from this array.
    (LC-1539)
'''

def solution(arr, k):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        missing = arr[mid] - mid - 1
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
        
    return low + k 


if __name__ == "__main__":
    arr = [2, 3, 4, 7, 11]
    k = 5
    # expected op = 9
    print(solution(arr, k))
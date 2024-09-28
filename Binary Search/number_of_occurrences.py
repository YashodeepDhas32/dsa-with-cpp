'''
    Given a sorted array Arr of size N and a number X, 
    you need to find the number of occurrences of X in Arr.
    (GFG)
'''

def findFirst(arr, n, x):
    low, high = 0, n-1
    first = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            first = mid
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    
    return first

def findLast(arr, n, x):
    low, high = 0, n-1
    last = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            last = mid
            low = mid + 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    
    return last

def solution(arr, n, x):
    if findFirst(arr, n, x) == -1:
        return 0
    else:
        return (findLast(arr, n, x) - findFirst(arr, n, x)) + 1


if __name__ == "__main__":
    Arr = [1, 1, 2, 2, 2, 2, 3]
    N = 7
    x = 2
    print(solution(Arr, N, x))
'''
    You are given a sorted array consisting of only integers where every element appears exactly twice, 
    except for one element which appears exactly once.
    Return the single element that appears only once.
    (LC-540)
'''

'''
    intuition:
    - check edge cases, either 1 element exist then return that, either first or last element is single element return first/last
    - run binary search, excluding first and last(since its already checked)
    - search step = check if mid'th element not equals mid-1'th and mid'th element not equals mid+1'th element, then thats single
    - elimination step = check if mid is even and mid+1'th element equals mid'th element or  
    - check if mid is odd and mid-1'th element equals mid'th element, then reduce increase low to mid + 1
    - else reduce high to mid - 1
'''
def solution(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n-1] != arr[n-2]:
        return arr[n-1]
    
    low, high = 1, n-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid + 1]:
            return arr[mid]
        else:
            if (mid % 2 == 0 and arr[mid+1] == arr[mid]) or (mid % 2 == 1 and arr[mid] == arr[mid-1]):
                low = mid + 1
            else:
                high = mid - 1
    return -1

if __name__ == "__main__":
    nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    # expected op = 2
    print(solution(nums))
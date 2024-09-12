'''
    You are given an array of size N. Rearrange the given array in-place such that 
    all the negative numbers occur before all non-negative numbers.
    (Maintain the order of all -ve and non-negative numbers as given in the original array).
    (GFG)
'''


'''
    intuition: (based on merge sort algorithm)
    - run basic merge sort for array
    - introduce i and j to find positive elements in both halves of array 
    - then reverse both positive halves and finally reverse the array between i and j-1
'''
def solution(arr, n):
    merge_sort(arr, 0, n-1)
    return

def merge_sort(arr, l, r):
    mid = (l + r) // 2
    if l < r:
        merge_sort(arr, l, mid)
        merge_sort(arr, mid + 1, r)
        merge(arr, l, mid, r)

def merge(arr, l, mid, r):
    i = l
    while i <= mid and arr[i] < 0:
        i += 1
    
    j = mid + 1
    while j <= r and arr[j] < 0:
        j += 1

    reverse(arr, i, mid)
    reverse(arr, mid + 1, j - 1)
    reverse(arr, i, j-1)

def reverse(arr, l, r):
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

if __name__ == '__main__':

    mylist = [-1, 3, -2, 4, -5, 6, 0, -3, 2]
    # expected o/p = [-1, -2, -5, -3, 3, 4, 6, 0, 2]
    solution(mylist, len(mylist))
    print(mylist)

'''
    Given an array of integers. Find the Inversion Count in the array.  
    Two elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.
    (GFG)
'''

'''
    intuition (using merge sort):
    - use merge sort code, just add count variable as extra variable
    - whenever the element from left half of sorted array is greater then element in right half of sorted array
    - increment count with mid - left + 1
    - return count as local variable (since global assignment is bad practice)
'''

def merge(arr, start, mid, end):
    left = start
    right = mid + 1
    temp = []
    cnt = 0

    while left <= mid and right <= end:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
            cnt += (mid - left + 1)
    
    while left <= mid:
        temp.append(arr[left])
        left += 1
    
    while right <= end:
        temp.append(arr[right])
        right += 1
    
    for i in range(start, end + 1):
        arr[i] = temp[i - start]

    return cnt


def merge_sort(arr, start, end):
    cnt = 0
    if start >= end:
        return cnt
    mid = ( start + end ) // 2
    cnt += merge_sort(arr, start, mid)    
    cnt += merge_sort(arr, mid + 1, end)
    cnt += merge(arr, start, mid, end)
    return cnt


def solution(arr):
    return merge_sort(arr, 0, len(arr)-1)

    
if __name__ == "__main__":
    
    mylist = [2, 4, 1, 3, 5]
    # expected o/p = 3 i.e = (2, 1), (4, 1), (4, 3)
    print(solution(mylist))
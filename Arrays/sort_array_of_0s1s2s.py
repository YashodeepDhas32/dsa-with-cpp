'''
    Given an array A[] consisting of only 0s, 1s, and 2s. 
    The task is to sort the array, i.e., put all 0s first, then all 1s and all 2s in last.
'''

'''
    intuition (uses dutch national flag algorithm):
    - keep low and mid on extreme left and high at extreme right
    - run loop till mid crosses high
    - handle Three major cases where mid is 0, or 1 or 2
'''
def solution(arr):    
    low, mid, high = 0, 0, len(arr)-1
    while(mid <= high):
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr


if __name__ == '__main__':
    my_list = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    # expected o/p = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
    print(solution(my_list))
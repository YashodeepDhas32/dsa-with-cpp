'''
    Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
    If target is not found in the array, return [-1, -1].
    You must write an algorithm with O(log n) runtime complexity.
    (LC-34)
'''

'''
    intuition:
    - run basic binary search algorithm, only thing to modify is look out for first occurence
    - first occurence would be in left half (left side), keep trimming right side until nums[mid] matches target
    - last occurence would be right half (right side), keep trimming left side until nums[mid] matches target
    - finally return both occurrences
'''
def findFirst(nums, low, high, target):
    first = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            first = mid
            high = mid - 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return first

def findLast(nums, low, high, target):
    last = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            last = mid
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return last


def solution(arr, target):
    n = len(arr)
    if findFirst(arr, 0, n-1, target) == -1:
        return [-1, -1]
    return [
        findFirst(arr, 0, n-1, target),
        findLast(arr, 0, n-1, target)
    ]

if __name__ == "__main__":
    mylist = [5,7,7,8,8,10]
    t = 8
    # expected op = [3, 4]
    print(solution(mylist, t))
'''
    Given an array of integers nums and an integer target, 
    return indices of the two numbers such that they add up to target.
    (LC-1)
'''

'''
    intuition (if return indices):
    - check if dict contains different of target and current array element.
    - else store the current array element.    
'''
def solution(arr, target) -> list[int]:
    mp = dict()
    for i in range(len(arr)):
        if target - arr[i] in mp:
            return [i, mp[target-arr[i]]]
        else:
            mp[arr[i]] = i

    return []


'''
    intuition (return true or false if exists or not):
    - sort the array
    - iterate until left < right.
    - check if sum of current left and current right element matches target, if yes return True
    - else reduce left pointer or right pointer accordingly
'''
def solution_two(arr: list, target) -> bool:
    arr.sort()
    left, right = 0, len(arr)-1

    while(left < right):
        if arr[left] + arr[right] == target:
            return True
        elif arr[left] + arr[right] > target:
            right -= 1
        else:
            left += 1

    return False


if __name__ == '__main__':
    nums = [1, 4, 45, 6, 10, 8]
    target = 16
    # expected o/p - [3, 4] or [4, 3]
    print(solution(nums, target))
    # expected o/p - True (sum exists)
    print(solution_two(nums, target))
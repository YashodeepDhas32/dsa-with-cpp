'''
    Given an array, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] 
    such that:
    - 0 <= a, b, c, d < n
    - a, b, c, and d are distinct.
    - nums[a] + nums[b] + nums[c] + nums[d] == target
    You may return the answer in any order.
    (LC-18)
'''

def solution(arr: list, target: int) -> list[list[int]]:
    result = []
    arr.sort()
    n = len(arr)

    for i in range(n):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1, n):
            if j > i+1 and arr[j] == arr[j-1]:
                continue
            
            k = j + 1
            l = n - 1
            while k < l:
                sm = arr[i] + arr[j] + arr[k] + arr[l]
                if sm > target:
                    l -= 1
                elif sm < target:
                    k += 1
                else:
                    result.append([arr[i], arr[j], arr[k], arr[l]])
                    k += 1
                    l -= 1
                    while k < l and arr[k] == arr[k-1]:
                        k += 1
                    while k < l and arr[l] == arr[l+1]:
                        l -= 1

    return result


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    # expected op = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    print(solution(nums, target))
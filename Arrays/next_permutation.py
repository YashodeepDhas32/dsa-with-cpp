'''
    Given an array of integers, find the next permutation of array.
    (LC - 31)
'''

'''
    intuition:
    - find the index(turing point) at which increasing numbers declined
    - handle the edge case if no turing point is found meaning its last permutation and reversing array will lead to first permutation
    - swap turning point element with next smallest element to that of turning point
    - reverse the rest of the array from index+1 to end
'''

def solution(arr):
    index = -1
    for i in range(len(arr)-2, -1, -1):
        if arr[i] < arr[i+1]:
            index = i
            break
    
    if index == -1:
        arr.reverse()
        return
    
    for i in range(len(arr)-1, index, -1):
        if arr[i] > arr[index]:
            arr[i], arr[index] = arr[index], arr[i]
            break

    arr[index+1:] = reversed(arr[index+1:])
    return


if __name__ == '__main__':
    mylist = [3, 1, 2]
    solution(mylist)
    # expected o/p = [3, 2, 1]
    print(f'Next permutation for mylist is = {mylist}')
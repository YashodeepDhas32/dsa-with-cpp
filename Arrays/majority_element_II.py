'''
    Given an integer array of size n, find all elements that appear more than [ n/3 ] times.
    LC - 229
'''

'''
    intuition (uses moore's voting algorithm):
    - keep 2 element variables prefereably as maxsize-1 and candidates counts 1 and 2 as 0
    - run loop till end of array, increment count if ele1 is same as current array element, same for ele2
    - if any of count1 and count2 is 0 then reassign new element to ele1 and ele2 and reassign counts to 1
    - run extra loop to check count of elements >= n/3 + 1, then add up the elements into result list
'''
import sys
def solution(arr):
    result = []
    count1, count2 = 0, 0
    ele1, ele2 = -sys.maxsize-1, -sys.maxsize-1
    for i in range(len(arr)):
        if ele1 == arr[i]:
            count1 += 1
        elif ele2 == arr[i]:
            count2 += 1
        elif count1 == 0:
            ele1 = arr[i]
            count1 = 1
        elif count2 == 0:
            ele2 = arr[i]
            count2 = 1
        else:
            count1 -= 1
            count2 -=1

    count1, count2 = 0, 0
    for i in range(len(arr)):
        if arr[i] == ele1:
            count1 += 1
        elif arr[i] == ele2:
            count2 += 1
    
    if count1 >= len(arr)//3 + 1:
        result.append(ele1)
    if count2 >= len(arr)//3 + 1:
        result.append(ele2)

    return result

if __name__ == '__main__':

    my_list = [1, 2, 3, 1, 1, 2, 1]
    # n//3 + 1 = 7//3 3
    # expected o/p = [1]
    print(solution(my_list))
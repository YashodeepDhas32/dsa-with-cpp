'''
    Given an array of positive integers, find all the leaders in the array. 
    An element of the array is considered a leader if it is greater than all the elements on its right side
    or if it is equal to the maximum element on its right side. The rightmost element is always a leader.
    (GFG)
'''
import sys

'''
    intuition:
    - run loop from end, store current max as smallest num
    - check if current num is smaller than max, if yes update max with current num
    - also append the current num to result and return the reversed list
'''
def solution(arr)-> list[int]:
    result = []
    maxnum = -sys.maxsize-1
    for i in range(len(arr)-1, -1, -1):
        if arr[i] > maxnum:
            maxnum = arr[i]
            result.append(arr[i])

    result = reversed(result)
    return result

if __name__ == '__main__':

    mylist = [16, 17, 4, 3, 5, 2]
    output = solution(mylist)
    # expected o/p = [17, 5, 2]
    print([x for x in output])
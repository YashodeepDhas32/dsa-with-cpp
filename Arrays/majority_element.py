'''
    Given an array nums of size n, return the majority element.
    The majority element is the element that appears more than [n / 2] times. 
    You may assume that the majority element always exists in the array.
    (LC-169)
'''

'''
    intuition (uses moore's voting algorithm):
    - keep element variable at 0th index initially and count as 0
    - run loop till end of array, increment count if next element is same, else decrement count
    - if count is 0 then reassign new element and reassign count to 1
    - (EXTRA)if majority element not always exits in the array, run extra loop to check count of element > n/2
'''
def solution(arr):
    element, count = arr[0], 0
    for i in range(len(arr)):
        if count == 0:
            element = arr[i]
            count = 1
        elif element == arr[i]:
            count += 1
        else:
            count -= 1

    return element


if __name__ == '__main__':
    my_list = [2, 2, 3, 3, 1, 2, 2]
    print(f"Majority element in list - {my_list}")

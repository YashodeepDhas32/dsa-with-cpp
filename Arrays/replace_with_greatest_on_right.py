'''
    Given an array, replace every element in that array with the greatest element 
    among the elements to its right, and replace the last element with -1.
    After doing so, return the array.
    LC(1299)
'''

'''
    intuition:
    - initialize prev_max as -1 and run a loop from end to start
    - check if current element is greater than prev_max, then swap prev_max and current element
    - else assign current element to prev_max and return the array
'''
def solution(arr):
    prev_max = -1
    for i in range(len(arr)-1, -1, -1):
        if arr[i] > prev_max:
            arr[i], prev_max = prev_max, arr[i]
        else:
            arr[i] = prev_max
            
    return arr


if __name__ == '__main__':

    mylist = [17, 18, 5, 4, 6, 1]    
    # expected o/p = [18,6,6,6,1,-1]
    print(solution(mylist))
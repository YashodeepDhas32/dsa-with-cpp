'''
    Given an unsorted array, return the length of the longest consecutive elements sequence.
    You must write an algorithm that runs in O(n) time.
    (LC-128)
'''

'''
    intuition: 
    - store all elements in set and initialize maxlen as 1 because every element in itself is a sequence
    - iterate over elements in set, and set count = 0
    - then check if item's previous element not exist, set count as 1 and x as item
    - then check every next element of the x eg- x=1 then check 2, 3, 4 exists and increase count
    - after checking, see if maxlen or count which is greater and assign it to maxlen
'''
def solution(arr, N):
    # edge case
    if N == 0:
        return 0
    
    st = set()
    for i in range(N):
        st.add(arr[i])

    maxlen = 1

    for item in st:        
        count = 0
        if not item - 1 in st:
            count = 1
            x = item
            while x + 1 in st:
                count = count + 1
                x = x + 1
                        
        maxlen = max(maxlen, count)

    return maxlen


if __name__ == '__main__':
    mylist = [0, 3, 7, 2, 5, 8, 4, 6 ,0, 1]
    # expected o/p = 9 [0,1,2,3,4,5,6,7,8]
    print(f'longest length = {solution(mylist, len(mylist))}')


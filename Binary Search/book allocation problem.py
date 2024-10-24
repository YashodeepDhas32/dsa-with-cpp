'''
    You have n books, each with arr[i] a number of pages. m students need to be allocated contiguous books, 
    with each student getting at least one book. Out of all the permutations, the goal is to find 
    the permutation where the sum of the maximum number of pages in a book allotted to a student should 
    be the minimum, out of all possible permutations.
    (GFG)
'''
import sys
def find_count(books, mid, n):
    total_of_pages, total_students = 0, 1
    for i in range(n):
        if total_of_pages + books[i] <= mid:
            total_of_pages += books[i]
        else:
            total_students += 1            
            total_of_pages = books[i]

    return total_students

'''
    intuition:
    - handle edge case where students(m) outnumber the totalnumber of books(n), return -1
    - determine range for search, low will be largest in array(books) and high will besummation of array
    - write student count funcn, set total pages as 0 and total students as 1
    - run loop to end of array, check if sum of total pages and ith page <= mid, if yes then add ith pages to total
    - else, increment total students and set total pages as current ith books page
    - return total students, compare that value with given m(students), if less than or equals, eliminate right half
    - else eliminate left half, finally return low, since we want minimum of max pages
'''
def solution(books, n, m):
    if m > n:
        return -1
    low, high = -sys.maxsize-1, 0
    for i in books:
        low = max(low, i)
        high += i

    while low <= high:
        mid = (low + high) // 2
        count_of_students = find_count(books, mid, n)
        if count_of_students <= m:
            high = mid - 1
        else:
            low = mid + 1
        
    return low

if __name__ == "__main__":
    books = [12, 34, 67, 90]
    n = 4
    m = 2
    # expected op = 113 i.e - 12, 34, 67 and 90 => 12+34+67=113
    print(solution(books, n, m))
'''
    You are given an integer array nums, an integer array queries, and an integer x.
    For each queries[i], you need to find the index of the queries[i]th occurrence of x in the nums array. 
    If there are fewer than queries[i] occurrences of x, the answer should be -1 for that query.
    Return an integer array answer containing the answers to all queries.
    (LC-3159)
'''

'''
    intuition:
    - initialize count as 0 and empty hashmap, then run a loop to traverse the array
    - check if current element equals x, if yes then increment count and assign hashmap of count current index
    - traverse through all mentioned queries, if current query(q) exists in hashmap, append the index in map to result
    - if not append -1
    - basically we store the { occurrence: index } and if occurrence exists in map we store index in result, else -1

'''
def solution(arr, queries, x):
    count = 0
    mp = {}
    for i in range(len(arr)):
        if arr[i] == x:
            count += 1
            mp[count] = i
    res = []
    for q in queries:
        if q in mp:
           res.append(mp[q]) 
        else:
            res.append(-1)

    return res


if __name__ == "__main__":
    nums = [1,3,1,7]
    queries = [1,3,2,4]
    x = 1
    # expected o/p = [0, -1, 2, -1]

    print(solution(nums, queries, x))
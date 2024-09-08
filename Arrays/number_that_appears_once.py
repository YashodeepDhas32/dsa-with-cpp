'''
        in list of numbers with all numbers appear twice, except one number
        find that Number that appears once (LC 136)
'''

# optimal approach using XOR works because of self cancellation property
# element ^ 0 = element 
# element ^ element = 0
def solution(arr):
    result = 0
    for i in range(0, len(arr)):
        result = result ^ arr[i]        

    return result

# brute force approach using hash map (dict)
def brute_force_approach(arr):
    temp = dict()
    for i in range(0, len(arr)):
        if arr[i] in temp:
            temp[arr[i]] += 1
        else:
            temp[arr[i]] = 1
        
    for key, value in temp.items():
        if value == 1:
            return key

    return -1

if __name__ == "__main__":
    my_list = [4, 1, 2, 3, 1, 2, 3, 5, 6, 6, 7, 7, 5]
    # expected o/p - 4
    print(f'Number that appears once - {solution(my_list)}')

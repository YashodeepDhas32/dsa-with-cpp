'''
    Return the count of maximum consecutive 1's from list
'''

def solution(arr):
    max = 0
    current_count = 0
    for i in range(0, len(arr)):
        if arr[i] == 1:
            current_count += 1
            if max < current_count:
                max = current_count
        else:
            current_count = 0
    return max



if __name__ == "__main__":

    my_list = [1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0]
    # expected o/p = 3
    print(f'maximum consecutive ones are - {solution(my_list)}')
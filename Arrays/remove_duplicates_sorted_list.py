# Given array of integers sorted in asceding order, remove duplicates such that each unique element appears only one


def remove_duplicates_in_sorted_list(arr):
    j = 0
    for i in range(1, len(arr)):        
        if arr[j] != arr[i]:
            arr[j+1] = arr[i]
            j += 1
        
    return j+1

if __name__ == '__main__':                  
    my_list = [0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(f"Unique Elments in sorted list - {remove_duplicates_in_sorted_list(my_list)}")
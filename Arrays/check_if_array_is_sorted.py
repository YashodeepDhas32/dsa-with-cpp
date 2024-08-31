# given the array of integers check if array is sorted in ascending order

def check_if_array_is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] >= arr[i-1]:
            pass
        else:
            return False
    return True


if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 12, 17]
    my_list_2 = [1, 4, 12, 17, 13, 31, 8]

    print(f"is my list sorted ? - {'Yes' if check_if_array_is_sorted(my_list) else 'No'}")
    print(f"is my list 2 sorted ? - {'Yes' if check_if_array_is_sorted(my_list_2) else 'No'}")
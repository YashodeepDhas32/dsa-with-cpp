# shift zeroes to end maintaining relative order of non zero items in list


def shift_zeros_to_end(arr):
    j = -1
    for i in range(0, len(arr)):
        if arr[i] == 0:
            j = i
            break

    if j == -1:
        return arr

    n = j + 1
    for i in range(n, len(arr)):
        if(arr[i] != 0 and arr[j] == 0):
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
            
    return arr


if __name__ == "__main__":
    my_list = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]

    print(shift_zeros_to_end(my_list))
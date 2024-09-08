def reverse_sublist(arr, start, end):
    while start < end:  
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_by_k_places(arr, k):
    n = len(arr)
    # since it will generate same array if k is greater than length of array
    k = k % n  

    reverse_sublist(arr, 0, k-1)
    
    reverse_sublist(arr, k, n-1)
    
    reverse_sublist(arr, 0, n-1)

    return arr

if __name__ == '__main__':
    k = 8
    my_list = [1, 2, 3, 4, 5, 6, 7]
    print(rotate_by_k_places(my_list, k))

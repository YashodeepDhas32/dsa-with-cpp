''' Find the second largest element in list '''

def find_second_largest(my_list):
    largest, second_largest  = my_list[0], -1
    for i in range(1, len(my_list)):
        if my_list[i] > largest:
            second_largest = largest
            largest = my_list[i]
            
        elif my_list[i] > second_largest and my_list[i] != largest:
            second_largest = my_list[i]
            
    return second_largest
    
    
if __name__ == "__main__":
    my_list = [1, 5, 2, 12, 7, 12, 3, 7, 4, 6, 1];
    print(f"second largest element - {find_second_largest(my_list)}")
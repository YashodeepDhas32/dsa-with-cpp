def find_max_in_list(myList):
    # if list contains no elements return
    if(len(myList) > 0):
        max_num = myList[0]
    else:
        return -1
    

    for i in range(0, len(myList)):
        if(myList[i] > max_num):
            max_num = myList[i]
        # print(myList[i])
    return max_num

if __name__ == "__main__":
    myList = [1, 13, 7, 15, 2]

    print(find_max_in_list(myList))
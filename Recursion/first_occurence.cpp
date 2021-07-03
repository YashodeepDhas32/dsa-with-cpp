// find index of first and last index of occurence of given element in an array
#include<iostream>
// O(n) time
int indexOfFirstOccurence(int arr[], int n, int x, int idx) {
    // base case
    if(idx == n) {
        return -1;
    }

    if(arr[idx] == x) {
        return idx;
    }          
    // linearly pair for next element  
    indexOfFirstOccurence(arr, n, x, idx+1);    
}

int lastIndexOfOccurence(int arr[], int n, int x, int idx) {
    // base case
    if(idx == n-1) {
        return idx;
    }

    int li = lastIndexOfOccurence(arr, n, x, idx+1);
    if(arr[li] == x) {
        return li;
    } else {
        return idx;
    }
    return -1;
}

int main() {
    int arr[] = {4, 3, 3, 5, 6, 3, 1, 2, 3};
    int n = sizeof(arr)/sizeof(arr[0]);
    int x = 3;
    std::cout << indexOfFirstOccurence(arr, n, x, 0) << "\n";
    std::cout << lastIndexOfOccurence(arr, n, x, 0) << "\n";
    return 0;
}

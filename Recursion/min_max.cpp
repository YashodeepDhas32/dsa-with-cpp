// find mininum and maximum item of array using recursion
#include<iostream>
int minOfArray(int arr[], int n, int idx) {
    // base case
    if(idx == n-1) {
        return arr[idx];
    }
    // find min in smaller sub array from idx + 1
    int mi = minOfArray(arr, n, idx+1);
    if(mi < arr[idx]) {
        return mi;
    } else {
        return arr[idx];
    }
}

int maxOfArray(int arr[], int n, int idx) {
    // base case
    if(idx == n-1) {
        return arr[idx];
    }
    // find max item in smaller subarray from idx+1
    int mx = maxOfArray(arr, n, idx+1);
    if(arr[idx] > mx) {
        return arr[idx];
    } else {
        return mx;
    }
}

int main() {
    int arr[] = {1, 12, 10, 4, 6};
    int n = sizeof(arr)/sizeof(arr[0]);
    std::cout << "Minimum of array = " << minOfArray(arr, n, 0) << "\n";
    std::cout << "Maximum of array = " << maxOfArray(arr, n, 0) << "\n";
    return 0;
}
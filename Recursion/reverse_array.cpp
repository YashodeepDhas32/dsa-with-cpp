#include<iostream>

void revArray(int arr[], int low, int high) {
    // base case
    if(low >= high)
        return;
    
    int temp = arr[low];
    arr[low] = arr[high];
    arr[high] = temp;
    revArray(arr, low+1, high-1);
}

int main() {
    int n;
    std::cin >> n;
    int arr[n];
    for(int i=0; i<n; i++)
        std::cin >> arr[i];

    int low = 0, high = n-1;
    revArray(arr, low, high);
    for(int i=0; i<n; i++)
        std::cout << arr[i] << " ";
    std::cout << "\n";
    return 0;
}
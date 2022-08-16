#include<iostream>
using namespace std;

int partition(int arr[], int left, int right) {
    // assume pivot
    int pivot = arr[right];
    // find that maybe index of pivot found so far
    int i = left-1;
    // compare and increment
    for(int j=left; j<=right-1; j++) {
        if(arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i+1], arr[right]);
    return i+1;
}

void quickSort(int arr[], int left, int right) {
    if(left < right) {
        // find pivotindex
        int pivotIndex = partition(arr, left, right);
        quickSort(arr, left, pivotIndex-1);
        quickSort(arr, pivotIndex+1, right);
    }
}

int main() {
    int n;
    cin >> n;
    int arr[n];
    for(int i=0; i<n; i++) cin >> arr[i];
    quickSort(arr, 0, n-1);
    for(int i=0; i<n; i++) cout << arr[i] << " ";
    return 0;
}
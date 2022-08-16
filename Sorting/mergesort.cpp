#include<iostream>

using namespace std;

void merge(int arr[], int left, int mid, int right) {
    // get sizes
    int n1 = mid-left+1;
    int n2 = right-mid;
    // init 2 arrays
    int arr1[n1];
    int arr2[n2];
    // populate the arrays
    for(int i=0; i<n1; i++) {
        arr1[i] = arr[left+i];
    }
    for(int i=0; i<n2; i++) {
        arr2[i] = arr[mid+1+i];
    }
    // init i, j and k
    int i=0, j=0, k=left;
    // compare and populate main array
    while(i<n1 && j<n2) {
        if(arr1[i] < arr2[j]) {
            arr[k] = arr1[i];
            i++; k++;
        }
        else {
            arr[k] = arr2[j];
            j++; k++;
        }
    }
    // merge left out values
    while(i<n1) {
        arr[k] = arr1[i];
        i++; k++;
    }
    while(j<n2) {
        arr[k] = arr2[j];
        j++; k++;
    }
}

void mergeSort(int arr[], int left, int right) {
    if(left < right) {
        int mid = (left+right)/2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid+1, right);
        merge(arr, left, mid, right);
    }    
}

int main() {
    int n;
    cin >> n;
    int arr[n];
    for(int i=0; i<n; i++) cin >> arr[i];

    mergeSort(arr, 0, n-1);
    for(int i=0; i<n; i++) cout << arr[i] << " ";
    return 0;
}
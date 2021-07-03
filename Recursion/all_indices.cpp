// return array/vector of all indexes of occurences of given element x in array
#include<iostream>
#include<vector>
void allIndicesOfArray(int arr[], int n, int x, int idx, std::vector<int>& store) {
    // base case
    if(idx == n) {
        return;
    }
    if(arr[idx] == x) {
        store.push_back(idx);
        allIndicesOfArray(arr, n, x, idx+1, store);                
    } else {
        allIndicesOfArray(arr, n, x, idx+1, store);
    }
}

int main() {
    int arr[] = {4, 2, 3, 8, 5, 3, 7, 4, 3, 2};
    int n = sizeof(arr)/sizeof(arr[0]);
    int x = 3;
    std::vector<int> store;  
    allIndicesOfArray(arr, n, x, 0, store);
    std::cout << "the indexes which hold " << x << " in array are: \n";
    for(auto i: store)
        std::cout << i << " ";
    std::cout << "\n";
    return 0;
}
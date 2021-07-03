#include<iostream>
#include<vector>
 
void insert(std::vector<int>& arr, int temp) {
    // base condition
    if(arr.size() == 0 or arr.back() <= temp) {
        arr.push_back(temp);
        return;
    }
    int val = arr.back();
    arr.pop_back();
    arr.push_back(temp);
    insert(arr, val);
    
}
// sort the array/vector using recursion
void sortArray(std::vector<int>& arr) {
    // base condition
    if(arr.size() == 1) {
        return;
    }
    int temp = arr.back();
    arr.pop_back();
    sortArray(arr);
    insert(arr, temp);
}

// 2 1 5 4
// temp = 4, 5, 1, 2
// insert(2), insert(1), insert(5), insert(4)
// arr = 1, 2, 4, 5
// val = 5

int main() {
    int arr[] = {2, 1, 5, 4};
    int n = sizeof(arr)/sizeof(arr[0]);
    std::vector<int> v(arr, arr+n);
    sortArray(v);
    // sorted array   
    for(auto i : v)
        std::cout << i << " ";
    std::cout << "\n";
    return 0;
}
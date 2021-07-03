#include<iostream>
#include<string>
// print target sum subsets [10, 20, 30] tar = 30 => 
void targetSumSubsets(int arr[], int idx, std::string subset, int target, int sum, int n) {
    // base case
    if(idx == n) {
        if(sum == target) {
            std::cout << subset << "\n";
        }
        return;
    }

    targetSumSubsets(arr, idx + 1, subset + std::to_string(arr[idx]) + ", ", target, sum + arr[idx], n);
    targetSumSubsets(arr, idx + 1, subset, target, sum, n);
}

int main() {
    int n, target;
    std::cin >> n >> target;
    int arr[n];
    for(int i=0; i<n; ++i)
        std::cin >> arr[i];

    targetSumSubsets(arr, 0, "", target, 0, n);

    return 0;
}
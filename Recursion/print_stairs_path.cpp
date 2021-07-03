#include<iostream>
// print stairs paths with jumps of 1 2 or 3
void printStairsPaths(int n, std::string path) {
    // base case
    if(n < 0) {
        return;
    }
    if(n == 0) {
        std::cout << path << "\n";
        return;
    }

    printStairsPaths(n - 1, '1' + path);
    printStairsPaths(n - 2, '2' + path);
    printStairsPaths(n - 3, '3' + path);
}

int main() {
    int n;
    std::cin >> n;
    printStairsPaths(n, "");
    std::cout << "\n";
    return 0;
}
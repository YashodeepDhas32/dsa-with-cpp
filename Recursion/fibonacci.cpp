#include<iostream>

// return the nth fibonacci number
int fibonacci(int n) {
    // base case
    if(n == 0) return 0;
    if(n == 1) return 1;

    return fibonacci(n - 1) + fibonacci(n - 2);
}

// 0 1 1 2 3 5 8 13 ...
int main() {
    int n;
    std::cin >> n;
    std::cout << fibonacci(n) << std::endl;

    return 0;
}

// int fibonacci(int n) {
//     int x = 0, y = 1;
//     int z = 0;
//     for(int i=1; i<n; i++) {
//         z = x + y;
//         x = y;
//         y = z;
//     }
//     return z;
// }


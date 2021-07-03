#include<iostream>
// O(n) time
int powerFunction(int x, int n) {
    // base case
    if(n == 0) {
        return 1;
    }
    return powerFunction(x, n-1) * x;
}
// O(log(n)) time, by squaring
int fasterPowerFunction(int x, int n) {
    // base case
    if(n == 0) {
        return 1;
    }
    else {
        // n is odd
        if(n % 2 == 1) {
            return fasterPowerFunction(x, n-1) * x;
        }
        // n is even
        else {
            int res = fasterPowerFunction(x, n/2);
            return res * res;
        }
    }
}

// 2^0 = 1
// 2^1 = 2
// 2^2 = 4
// 2^3 = 8
// 2^8 = 256 => (8 is even, 8/2=4) =>2^4(16) * 2^4(16) => 2^8(256) => fasterPowerFunction()

int main() {
    // number and exponent x^n
    int x, n;
    std::cin >> x >> n; 
    std::cout << powerFunction(x, n) << "\n";
    std::cout << fasterPowerFunction(x, n) << "\n";
    return 0;
}
// any number passed `n` returns to 1 after performing certain conditional based operations
#include<iostream>

void hailstone(int n) {
    std::cout << n << "\n";
    // base case
    if(n == 1) {
        return;
    }
    else {
        // n is even
        if(n % 2 == 0) {
            return hailstone(n / 2);
        }
        else {
            return hailstone(3 * n + 1);
        }
    }
}

int main() {
    int n;
    std::cin >> n;
    std::cout << "collatz sequence: \n";
    hailstone(n);
    return 0;
}
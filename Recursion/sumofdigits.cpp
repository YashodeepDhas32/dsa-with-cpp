#include<iostream>

int recursiveSum(int n) {
    // base case
    if(n < 10)
        return n;

    return recursiveSum(n / 10) + (n % 10);
}

// recursiveSum(253)
// recursiveSum(253 / 10) + (253 % 10)
// recursiveSum(25 / 10) + (25 % 10) + 3
// recursiveSum(2 / 10) + (2 % 10) + 5 + 3
// 2 < 10 return 2+5+3 => 10

// find sum of digits of number 253 => 2+5+3 => 9
int iterativeSum(int n) {
    int sum = 0;
    while(n!=0) {
        sum += n % 10;
        n = n / 10;
    }
    return sum;
}

// 253 % 10 => 3
// 253 / 10 => 25
// 25 % 10 => 5
// 25 / 10 => 2
// 2 % 10 => 2
// 2 / 10 => 0 break;

int main() {
    int n;
    std::cin >> n;
    std::cout << iterativeSum(n) << "\n";
    return 0;
}
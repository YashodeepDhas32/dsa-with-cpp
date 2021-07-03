#include<iostream>
// mystery recursion
int mysteryFunction(int n) {
    // base case
    if(n < 10) {
        return n;
    }
    else {
        int a = n / 10;
        int b = n % 10;
        return mysteryFunction(a + b);
    }
}

int main() {

    int n;
    std::cin >> n;

    std::cout << mysteryFunction(n) << "\n";
    return 0;
}
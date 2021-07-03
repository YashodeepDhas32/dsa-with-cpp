// factorial of number n
#include<iostream>

int factorial(int n) {
    // base case
    if(n==0)
        return 1;  

    // not a tail recursive as after calling, need to multiply with `n`
    return n * factorial(n - 1);
}

int factorialTail(int n, int k=1) {
    // base case
    if(n==0)
        return k;

    // tail recursive function as no multiply(*) or other operation after factorialTail() 
    return factorialTail(n - 1, k * n);
}

int main() {
    int n;
    std::cin >> n;
    int fact = factorial(n);
    std::cout << "factorial of " << n << " is " << fact << "\n";
    int factTail = factorialTail(n);
    std::cout << "factorial using tail recursion of " << n << " is " << factTail << "\n"; 
    return 0;
}

// iterative
// int factorial(int n) {
//     static int fact=1;
//     if(n==0)
//         return 1;
    
//     for(int i=n; i>0; i--) {
//         fact *= i;
//     }
//     return fact;
// }

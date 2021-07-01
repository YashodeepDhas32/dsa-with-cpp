#include<iostream>

void fun(int n) {
    // base case
    if(n < 1)
        return;
    else {
        std::cout << n << " ";
        fun(n-1);
        std::cout << n << " ";
    }
}

int main() {
    int n;
    std::cin >> n;
    fun(n);
    std::cout << std::endl;
    return 0;
}
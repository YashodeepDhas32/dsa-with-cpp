#include<iostream>

int ntoOne(int n) {
    if(n<=0)
        return n;
    // for n to 1
    // std::cout << n << " ";
    ntoOne(n-1);
    // 1 to n
    std::cout << n << " ";
}

int main() {
    int n;
    std::cin >> n;
    ntoOne(n);
    std::cout << std::endl;
    return 0;
}
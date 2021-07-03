#include<iostream>

int fun(int n=5, int i=1);

int main() {
    fun();
    return 0;
}

// in tail recursion last operation of function is recursive call
int fun(int n, int i) {
    if(n <= 0)
        return n;
    std::cout << i << " ";
    fun(n-1, i+1);
}

#include<iostream>
// tower of hanoi

void TOH(int n, char src, char dest, char aux) {
    // base case
    if(n == 1) {
        std::cout << "Shift disk " << n << " from " << src << " to " << dest <<"\n";
        return;
    }
    TOH(n-1, src, aux, dest);
    std::cout << "shift disk " << n << " from " << src <<" to " << dest << "\n";
    TOH(n-1, aux, dest, src);
}
// 2
// toh(1, a, , b)
int main() {

    int n;
    std::cin >> n;
    TOH(n, 'A', 'C', 'B');
    
}
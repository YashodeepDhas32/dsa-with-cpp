/* Given a rope of length n, you need to find the maximum number of pieces
you can make such that the length of every piece is in set {a, b, c} for
the given three values a, b, c */
#include<iostream>
#include<algorithm>

int maxCuts(int n, int a, int b, int c) {
    // base cases
    if(n == 0) return 0;
    if(n < 0) return -1;
    int res = std::max({maxCuts(n-a, a, b, c), maxCuts(n-b, a, b, c), maxCuts(n-c, a, b, c)});
    if(res == -1) return -1;
    return res + 1;
}
// time => O(3^n)
int main() {
    int n;
    std::cin >> n;
    int a, b, c;
    std::cin >> a >> b >> c;
    // the maximum number of pieces
    std::cout << maxCuts(n, a, b, c) << std::endl;
    return 0;
}
#include<iostream>
// print all possible maze paths without jumps
void printMazePaths(int sr, int sc, int dr, int dc, std::string paths) {
    // base case
    if(sr == dr and sc == dc) {
        std::cout << paths << "\n";
        return;
    }

    // horizontal paths
    if(sc < dc) {
        printMazePaths(sr, sc + 1, dr, dc, paths + "h");
    }
    // vertical paths
    if(sr < dr) {
        printMazePaths(sr + 1, sc, dr, dc, paths + "v");
    }
}

int main() {
    int n, m;
    std::cin >> n >> m;
    printMazePaths(1, 1, n, m, "");
    std::cout << "\n";
    return 0;
}
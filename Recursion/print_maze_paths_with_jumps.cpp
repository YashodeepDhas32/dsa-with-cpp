#include<iostream>

// print all possible maze paths with jumps

void printMazePathsWithJumps(int sr, int sc, int dr, int dc, std::string paths) {
    // base case
    if(sr == dr and sc == dc) {
        std::cout << paths << "\n";
        return; 
    }

    // horizontal jumps
    for(int jumps=1; jumps <= dc - sc; jumps++) {
        printMazePathsWithJumps(sr, sc + jumps, dr, dc, paths + "h" + std::to_string(jumps));
    }
    // vertical jumps
    for(int jumps=1; jumps <= dr - sr; jumps++) {
        printMazePathsWithJumps(sr + jumps, sc, dr, dc, paths + "v" + std::to_string(jumps));
    }
    // diagonal jumps
    for(int jumps=1; jumps <= dc - sc and jumps <= dr - sr; jumps++) {
        printMazePathsWithJumps(sr + jumps, sc + jumps, dr, dc, paths + "d" + std::to_string(jumps));
    }

}
int main() {
    int n, m;
    std::cin >> n >> m;
    printMazePathsWithJumps(1, 1, n, m, "");
    std::cout << "\n";
    return 0;
}
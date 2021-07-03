#include<iostream>
#include<vector>
#include<string>
// maze paths with jumps problem
std::vector<std::string> getMazePathsWithJumps(int sr, int sc, int dr, int dc, int& count) {
    // base case
    if(sr == dr and sc == dc) {
        std::vector<std::string> bpaths;
        bpaths.push_back("");
        count++;
        return bpaths;
    }
    std::vector<std::string> hPaths;
    std::vector<std::string> vPaths;
    std::vector<std::string> dPaths;
    std::vector<std::string> paths;

    // horizontal jumps
    for(int hjump=1; hjump <= dc - sc; hjump++) {
        hPaths = getMazePathsWithJumps(sr, sc + hjump, dr, dc, count);
        for(auto hpath : hPaths) {
            paths.push_back("h" + std::to_string(hjump) + hpath);
            // count++;

        }
    }
    // vertical jumps
    for(int vjump=1; vjump <= dr - sr; vjump++) {
        vPaths = getMazePathsWithJumps(sr + vjump, sc, dr, dc, count);
        for(auto vpath : vPaths) {
            paths.push_back("v" + std::to_string(vjump) + vpath);
            // count++;

        }
    }
    // diagonal jumps
    for(int djump=1; djump <= dr - sr and djump <= dc - sc; djump++) {
        dPaths = getMazePathsWithJumps(sr + djump, sc + djump, dr, dc, count);
        for(auto dpath : dPaths) {
            paths.push_back("d" + std::to_string(djump) + dpath);
            // count++;
        }
    }

    return paths;
}

int main() {
    int n, m;   // destination row and destination column
    std::cin >> n >> m;
    int count = 0;
    std::vector<std::string> mazepaths = getMazePathsWithJumps(1, 1, n, m, count);
    for(auto mp : mazepaths) {
        std::cout << mp << "\n";
    }
    std::cout << "\n";
    std::cout << "total possible paths: " << count << "\n";
    
    return 0;
}
#include<iostream>
#include<vector>

// get all the possible maze paths from source to expected destination
std::vector<std::string> getMazePaths(int sr, int sc, int dr, int dc) {
    // base case
    if(sr == dr and sc == dc) {
        std::vector<std::string> bpath;
        bpath.push_back("");
        return bpath;
    }

    std::vector<std::string> hPaths;
    std::vector<std::string> vPaths;
    
    if(sc < dc) {
        hPaths = getMazePaths(sr, sc + 1, dr, dc);
    }
    if(sr < dr) {
        vPaths = getMazePaths(sr + 1, sc, dr, dc);
    }
    std::vector<std::string> paths;
    for(auto hpath : hPaths) {
        paths.push_back("h" + hpath);
    }
    for(auto vpath : vPaths) {
        paths.push_back("v" + vpath);
    }
    return paths;
}
int main() {
    int n, m;
    std::cin >> n >> m;
    std::vector<std::string> mazepaths = getMazePaths(1, 1, n, m);
    for(auto mp : mazepaths) {
        std::cout << mp << " ";
    }
    std::cout << "\n";
    return 0;
}
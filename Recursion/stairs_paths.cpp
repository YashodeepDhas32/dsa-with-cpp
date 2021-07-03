#include<iostream>
#include<vector>
// get all paths to 0th stair from nth stair by using 1, 2 and 3 steps/jumps
std::vector<std::string> getStairsPath(int n) {

    // base case
    if(n == 0) {
        std::vector<std::string> result;
        result.push_back("");
        return result;

    }
    if(n < 0) {
        std::vector<std::string> result;
        return result;
    }
    
    std::vector<std::string> path1 = getStairsPath(n-1);
    std::vector<std::string> path2 = getStairsPath(n-2);
    std::vector<std::string> path3 = getStairsPath(n-3);
    
    std::vector<std::string> paths;

    for(auto p1: path1) {
        paths.push_back(p1 + '1');
    }
    for(auto p2: path2) {
        paths.push_back(p2 + '2');
    }
    for(auto p3: path3) {
        paths.push_back(p3 + '3');
    }
    
    return paths;
}

int main() {
    int n;  // number of stairs
    std::cin >> n;
    std::vector<std::string> allpaths = getStairsPath(n);
    for(auto it : allpaths) {
        std::cout << it << " ";
    }
    std::cout << std::endl;
    return 0;
}
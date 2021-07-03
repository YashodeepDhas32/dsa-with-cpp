// given a string generate all its possible subsets/subsequences
#include<iostream>
// "ABC" = '' 'C' 'B' 'BC' 'A' 'AC' 'AB' 'ABC'
void subsets(std::string str, std::string currstr="", int idx=0) {
    // base case
    if(idx == str.length()) {
        std::cout << "'" << currstr << "'" << " ";
        return;
    }

    subsets(str, currstr, idx+1);
    subsets(str, currstr+str[idx], idx+1);
}

int main() {
    std::string str;
    std::cin >> str;
    subsets(str);
    std::cout << std::endl;
    return 0;
}
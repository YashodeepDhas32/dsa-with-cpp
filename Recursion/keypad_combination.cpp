#include<bits/stdc++.h>
// https://ideone.com/ow05TO using BFS

// Get Keypad code combinations
void getKPC(std::string strarr[], std::string ip, std::string currstr) {
    // base case
    if(ip.length() == 0) {
        std::cout << currstr << " ";
        return;
    }

    char fchar = ip.at(0);
    std::string rstr = ip.substr(1);

    std::string it = strarr[fchar - '0'];//pqrs => taking '6' - '0' convert to number
    for(int i=0; i<it.length(); i++) {
        char option = it.at(i);
        getKPC(strarr, rstr, currstr+option);//option for p,q,r,s
    }
    
}
// 678 => 6+78 => pqrs+tuvwx => and so on...
int main() {
    std::string strarr[] = {".;", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tu", "vwx", "yz"};
    std::string ip;
    std::cin >> ip;
    
    getKPC(strarr, ip, "");
    std::cout << std::endl;
    return 0;
}
// euler path recursive tree
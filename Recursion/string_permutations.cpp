#include<iostream>
// print all the permutations of given string
void printPermutations(std::string ip, std::string op) {
    // base case
    if(ip.length() == 0) {
        std::cout << op << "\n";
        return;
    }
    for(int i=0; i<ip.length(); i++) {
        char ipchar = ip.at(i);
        std::string lstr = ip.substr(0, i);
        std::string rstr = ip.substr(i + 1);
        std::string remstr = lstr + rstr;
        printPermutations(remstr, op + ipchar);
    }
}
// permutations count => str.length()! => factorial of length of string
int main() {
    std::string ip;
    std::cin >> ip;
    std::cout << "Permutations are :" << "\n";
    printPermutations(ip, "");
    return 0;
}
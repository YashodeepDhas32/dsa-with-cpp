#include<iostream>

void printEncodings(std::string ip, std::string op) {
    // base case
    if(ip.length() == 0) {
        std::cout << op << "\n";
        return;
    }
    // first number
    int code1 = ip[0] - '0';
    char atcode1 = char('a' + code1 - 1);
    // first 2 numbers
    int code2 = stoi(ip.substr(0, 2));
    char atcode2 = char('a' + code2 - 1);

    if(code1 != 0) {
        printEncodings(ip.substr(1), op + atcode1);
    }
    if(code2 >= 10 and code2 <= 26) {
        printEncodings(ip.substr(2), op + atcode2);
    }
}

int main() {
    std::string ip;
    std::cin >> ip;
    printEncodings(ip, "");
    return 0;
}
// check whether string is palindrome or not
#include<iostream>
// racecar, nitin, madam, civic, rotor, malayalam
// recursive approach
bool palindrome(std::string somestr, int low, int high) {
    //base case
    if(low >= high)
        return true;
    if(somestr[low] != somestr[high])
        return false;
    palindrome(somestr, low+1, high-1);
}   

int main() {
    std::string somestr;
    std::cin >> somestr;
    int low = 0, high = somestr.length() - 1;
    palindrome(somestr, low, high) ? std::cout << "Its a palindrome String!\n" : std::cout << "its not a palindrome :(\n";
    return 0;
}

// iterative approach
// bool palindrome(std::string somestring) {
//     int low = 0, high = somestring.length() - 1;
//     while(low <= high) {
//         if(somestring[low] == somestring[high]) {
//             low++;
//             high--;
//         } else {
//             return false;
//         }
//     }
//     if(low > high) return true;
// }

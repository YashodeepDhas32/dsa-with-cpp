// delete middle element from stack
#include<iostream>
#include<stack>

void pushBacks(std::stack<int>& stk, int k) {
    // base case
    if(k == 1) {
        stk.pop();
        return;
    }
    int temp = stk.top();
    stk.pop();
    pushBacks(stk, k-1);
    stk.push(temp);
    return;
}

void deleteMid(std::stack<int>& stk, int size) {
    // base case
    if(stk.size() == 0) {
        return;
    }
        
    int k = stk.size()/2 + 1;
    pushBacks(stk, k);
    return;
}
int main() {
    std::stack<int> stk;
    stk.push(2);
    stk.push(1);
    stk.push(3);
    stk.push(5);
    stk.push(4);

    deleteMid(stk, stk.size());

    while(!stk.empty()) {
        std::cout << stk.top() << "\n";
        stk.pop();
    }
    return 0;
}
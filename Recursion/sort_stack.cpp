#include<iostream>
#include<stack>
// BASE CONDITION - HYPOTHESIS - INDUCTION
void insert(std::stack<int>& stk, int temp) {
    // base case
    if(stk.size() == 0 or stk.top() <= temp) {
        stk.push(temp);
        return;
    }
    int topval = stk.top();
    stk.pop();
    stk.push(temp);
    insert(stk, topval);
}
// sort stack in descending order using recursion
void sortStack(std::stack<int>& stk) {
    // base case
    if(stk.size() == 1) {
        return;
    }   
    int top = stk.top();
    stk.pop();
    sortStack(stk);
    insert(stk, top);    
}
// initial stk = 2, 1, 5, 4
// top/temp = 4, 5, 1, 2
// insert(top=2), insert(top=1), insert(top=5), insert(top=4)  
// stk = 1, 2, 4, 5
// topval = 5

int main() {
    std::stack<int> stk;
    stk.push(2);
    stk.push(1);
    stk.push(5);
    stk.push(4);
    sortStack(stk);
    while(!stk.empty()) {
        int temp = stk.top();
        stk.pop();
        std::cout << temp << "\n";
    }
    
    return 0;
}
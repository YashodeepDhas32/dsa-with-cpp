#include<iostream>
#include<queue>

void frontToLast(std::queue<int>& q, int size) {
    // base case
    if(size <= 0)
        return;
    // pop front element and push it to last
    q.push(q.front());
    q.pop();
    // recursively push all front elements to last
    frontToLast(q, size-1); 
}

void pushInQueue(std::queue<int>& q, int temp, int size) {
    // base case
    if(q.empty() || size == 0) {
        q.push(temp);
        return;
    }
    else if(temp <= q.front()) {
        q.push(temp);
        frontToLast(q, size);//param size ^
    }
    // temp is greater
    else {
        q.push(q.front());
        q.pop();
        pushInQueue(q, temp, size-1);
    }
}

void sortQueue(std::queue<int>& q) {
    // base case
    if(q.empty()) {
        return;
    }
    int front = q.front();
    q.pop();
    sortQueue(q);
    pushInQueue(q, front, q.size());   
}
// init q = 1, 5, 4
// popped = 1, 5, 4
// insert(temp=4, size=0), insert(temp=5, size=1), insert(temp=1,size=2)
// f q = 1, 4, 5 
int main() {
    std::queue<int> q;
    q.push(2);
    q.push(1);
    q.push(5);
    q.push(4);
    sortQueue(q);
    while(!q.empty()) {
        std::cout << q.front() << "\n";
        q.pop();        
    }
    return 0;
}
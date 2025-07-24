#include <iostream>
#include <typeinfo>
#include <vector>
#include "../../Learn C++/LinkedList.h"

using namespace std;

class MinStack {
private:
    vector<pair<int,int>> stack;
    // [ (val₀, min₀), (val₁, min₁), (val₂, min₂), ... ]

public:
    MinStack() {
        
    }
    
    void push(int val) {
        int min_val = getMin();
        if (stack.empty() || min_val > val) {
            min_val = val;
        }
        stack.push_back({val, min_val});        
    }
    
    void pop() {
        stack.pop_back();
    }
    
    int top() {
        // python
        // ==> return False if stack.empty() else stack.back()[0]
        return stack.empty() ? -1 : stack.back().first;
    }
    
    int getMin() {
        return stack.empty() ? -1 : stack.back().second; 
    }
};
//////////////////////////////////////////////////////////////////
int main() {
    MinStack minStack;
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);

    cout << minStack.getMin() << endl; 
    // ==> -3

    minStack.pop();

    cout << minStack.top() << endl;     
    // ==> 0
    cout << minStack.getMin() << endl;  
    // ==> -2

    return 0;
}
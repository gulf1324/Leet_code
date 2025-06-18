#include <iostream>
using namespace std;

// using copy of a passed value(r-value, l-value)
string modifyString(string s) {
    s = s.substr(0, 5);
    return s;
}

// directly editing the referenced value(only l-value)
string modifyStringRef(string &s) {
    s = s.substr(0, 5);
    return s;
}

int main() {
    string s = "hello world";
    
    // no ref, using copy of a l-value
    string result = modifyString(s);
    cout << "Returned: " << result << endl; // >>> hello 
    cout << "Original: " << s << endl; // >>> hello world
    
    // directly editing the referenced l-value 
    string result2 = modifyStringRef(s);
    cout << "Returned: " << result2 << endl; // >>> hello 
    cout << "Original: " << s << endl; // >>> hello 
}

// l-value => allocated on a memory, has name 
// r-value => temp, has no name

// more)
// r-value can only be passed as const value 
// => editing a temporary value is a waste
// const string& s 
// const string&& s

// const 붙이면 참조하든 안 하든 l-value, r-value 모두 넣을 수 있음
// const 안 붙이면 
//  - 참조 안할 때는 l-value, r-value 넘길 수 있음
//  - 참조할 때는 l-value만 넘길 수 있음

#include <iostream>
#include <typeinfo>
using namespace std;

/////////////////////////////////////////////////////////////////////////////////////
// Wrong
class Solution {
public:
    int longestValidParentheses(string s) {
        int maxLength = 0;
        int currLength = 0;
        int isOpen = 0;

        for (int i = 0; i < s.size(); i++) {
            // cout << "s[i] " << s[i] << " type " << typeid(s[i]).name() << endl;
            
            // if s is vector<string>, like {"(", "abc", ")"}, use ""
            // if s is a string(const char*), like "(()", use '' 
            // "" for string, '' for char
            
         // if (s[i] == "(" ) { ... } ==> (X)
            if (s[i] == '(' ) {    // ==> (O)
                isOpen++;
                currLength++;
            }
            else if (s[i] == ')' ) {
                if (isOpen > 0) {
                    isOpen--;
                    currLength++;
                    if (isOpen == 0) {
                        maxLength = max(maxLength, currLength);
                    }
                }
                else {
                    currLength = 0;
                    isOpen = 0;
                }
            }
            cout << " i " << i << " currLength " << currLength << endl;
        }
        return maxLength;
    }
};

/////////////////////////////////////////////////////////////////////////////////////
// Correct
// Two-Pass Linear Scan (No Stack, No DP)
class Solution2 {
public:
    int longestValidParentheses(string s) {
        int maxLength = 0;

        // Left to right
        int open = 0, close = 0;
        for (char c : s) {
            if (c == '(') open++;
            else close++;
            
            if (open == close) {
                maxLength = max(maxLength, 2 * close);
                }
            else if (close > open) {
                open = close = 0;
            }
        }

        // Right to left
        open = close = 0;
        for (int i = s.size() - 1; i >= 0; --i) {
            if (s[i] == '(') open++;
            else close++;
            
            if (open == close) {
                maxLength = max(maxLength, 2 * open);
            }
            else if (open > close) {
                open = close = 0;
            }
        }

        return maxLength;
    }
};
/////////////////////////////////////////////////////////////////////////////////////

int main() {
    Solution2 solution;
    // string s = "(()";
    // >>> 2
    // string s = ")()())";
    // >>> 4
    string s = "()(())";
    // >>> 6
    // string s = "()(()";
    // >>> 2
    int result = solution.longestValidParentheses(s);
    cout << "Longest valid parentheses length: " << result << endl;
    return 0;
}
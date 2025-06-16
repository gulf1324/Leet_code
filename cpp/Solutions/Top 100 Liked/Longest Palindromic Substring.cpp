#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        if (n < 2) return s;

        int start = 0;
        int maxLength = 1;

        // 초기화; 조건; 증감
        for (int i = 0; i < n; i++) {
            // Odd length palindromes
            int left = i;
            int right = i;
            while (left >= 0 && right < n && s[left] == s[right]) {
                if (right - left + 1 > maxLength) {
                    start = left;
                    maxLength = right - left + 1;
                }
                left--;
                right++;
            }

            // Even length palindromes
            left = i, right = i + 1;
            while (left >= 0 && right < n && s[left] == s[right]) {
                if (right - left + 1 > maxLength) {
                    start = left;
                    maxLength = right - left + 1;   // 길이 계산
                }
                left--;
                right++;
            }
        }

        // substring 추출 
        // start는 시작 인덱스, length는 길이
        // ex) s = "babad", start = 0, maxLength = 3
        // >>> bab
        return s.substr(start, maxLength);
    }
};

// Example usage:
int main() {
    Solution sol;
    string s = "babad";
    string result = sol.longestPalindrome(s);
    cout << result << endl; // Output: "bab" or "aba"
    return 0;
}
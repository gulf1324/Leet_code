#include <iostream>
#include <unordered_set>
#include <algorithm> // For sort
#include <typeinfo>
// using namespace std; <== not good (?)

////////////////////////////////////////////////////////////////////////////////////////////////////
// sliding window, obviously
class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        if (s.size() == 1) return 1;
        
        std::unordered_set<char> seen;
        int p = 0;
        int q = 0;
        int maxLength = 0;

        while (q < s.size()) {
            // .find()는 finds char, returns .end() when not found.
            // ==> check if char is already in the set.
            if (seen.find(s[q]) == seen.end()) {
                seen.insert(s[q]);
                maxLength = std::max(maxLength, q-p+1);
                q++;
            }
            else {
                seen.erase(s[p]);
                p++;
            }
        }
        return maxLength;
    }
};
//////////////////////////////////////////////////////////////////////////////
// Constraints : s consists of English letters, digits, symbols and spaces.
// ==> ASCII
// char is int in c++
//   ex) charIndex['b'] ==  charIndex[98]   (ASCII code)

class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        // ASCII 문자 집합의 크기
        std::vector<int> charIndex(128,-1); 
        
        int left=0;
        int maxlength=0;
    
        for(int i=0; i < s.length(); i++){
            
            if(charIndex[s[i]] >= left)            
            {
                left = charIndex[s[i]]+1;
            }
            
            charIndex[s[i]]=i;
            maxlength = std::max(maxlength, i-left+1);
          
        }
        return maxlength;
    }
};
//////////////////////////////////////////////////////////////////////////////
int main() {
    Solution solution;
    std::string s = "pwwkew";
    int result = solution.lengthOfLongestSubstring(s);
    std::cout << "Longest unique-charactered-substring: "<< result << std::endl;
    // >>> 3
    // >> (abc)
    return 0;
}
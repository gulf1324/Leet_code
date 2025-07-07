#include <iostream>
#include <vector>
#include <algorithm> // For sort
using namespace std;

////////////////////////////////////////////////////////////////////////////////////////////////////
// Constraints : in-place, O(1)
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> res;
        
        if (s.size() < p.size()) {
            return res;
        }

        vector<int> s_count(26, 0), p_count(26, 0);

        // c-'a' 
        // a부터 몇 번째 문자인지 ==> 0~25 사이의 정수로 저장
        // complete p_count vector for comparison with s_count vector
        for (char c : p) p_count[c - 'a']++;


        for (int i = 0; i < s.size(); i++) {
            s_count[s[i] - 'a']++;

            if (i >= p.size())
                s_count[s[i - p.size()] - 'a']--;

            // **in each for loop, compare s_count & p_count vector**
            // i - p.size() + 1 ==> "starting" index
            if (s_count == p_count)
                res.push_back(i - p.size() + 1);
        }

        return res;
    }
};
//////////////////////////////////////////////////////////////////
int main() {
    Solution solution;
    string s = "cbaebabacd";
    string p = "abc";
    vector<int> result = solution.findAnagrams(s, p);
    cout << "Starting index : {";
    
    for (size_t i = 0; i < result.size(); ++i) {
        if (i == 0) {
        cout << result[i];
        } 
        else {
            cout << "," << result[i];
        }
    }
    cout << "}" <<endl;
    // >>> {0, 6}
    return 0;
}
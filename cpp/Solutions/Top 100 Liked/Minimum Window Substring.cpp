#include <iostream>
#include <typeinfo>
#include <unordered_map>
#include <vector>
using namespace std;

/////////////////////////////////////////////////////////////////////////////////////
// Constraints: O(m+n) time
// m = s.size(), n = t.size()

// Solution ==> nested while loop for two-pointer-movement
class Solution {
public:
    string minWindow(string s, string t) {
        if (s.length() < t.length() || s.empty() || t.empty()) {
            return "";
        }
        int count[128] = {0}; // Stack, slightly faster, nost safe when gets bigger
        // vector<int> count(128, 0); // Heap, slightly slower, safe when gets bigger
        int required = 0;
        
        // t의 각 문자 개수 세기
        for (char c : t) {
            if (count[c] == 0) required++; // 새로운 문자면 required 증가
            count[c]++;
        }
        
        int left = 0, right = 0;
        int formed = 0; // 조건을 만족한 문자 종류 수
        int minLen = INT_MAX, start = 0;
        
        while (right < s.length()) { // for문으로 해도 상관 없이 동일
            // 오른쪽 문자 처리
            char rightChar = s[right];
            count[rightChar]--;
            
            // 이 문자가 필요한 개수를 정확히 만족했는지 체크
            if (count[rightChar] == 0) {
                formed++;
            }
            
            // 모든 조건을 만족한 상태일때만;
            // ==> 왼쪽 포인터 이동하며 최소화
            while (left <= right && formed == required) {
                // 더 작은 윈도우 발견시 업데이트
                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    start = left;
                }
                
                // 왼쪽 문자 제거
                char leftChar = s[left];
                count[leftChar]++;
                // 제거했을때 필요한 문자가 부족해졌는지 체크
                if (count[leftChar] > 0) {
                    formed--;
                }
                // left를 계속 오른쪽으로 이동
                left++;
            }
            
            right++;
        }
        
        return minLen == INT_MAX ? "" : s.substr(start, minLen);
    }
};
/////////////////////////////////////////////////////////////////////////////////////

int main() {
    Solution solution;
    string s = "ADOBECODEBANC";
    string t = "ABC";

    string result = solution.minWindow(s, t);
    cout << "Minimum window substring: " << result << endl;
    return 0;
}

/**
 * 1. first case of nested while loop : "ADOBEC" "minLen = 6",
 *  1-1. shrink left : "DOBEC" → outer loop again 
 * 2. "DOBECO" → "DOBECOD" → "DOBECODE" → "DOBECODEB" → "DOBECODEBA"
 * 3. second case of nested while loop : "DOBECODEBA" 
 *  3-1. shrink left : "OBECODEBA" → "BECODEBA" → "ECODEBA" → "CODEBA" "minLen = 6" → "ODEBA" → outer loop again 
 * 4. "ODEBA" → "ODEBAN" → "ODEBANC"
 * 5. third case of nested while loop : "ODEBANC" 
 *  5-1. shrink left : "DEBANC" → "EBANC" "minLen = 5" → "BANC" "minLen = 4" → "ANC" → outer loop again
 * 6. all while loops condition not met; return result
 */
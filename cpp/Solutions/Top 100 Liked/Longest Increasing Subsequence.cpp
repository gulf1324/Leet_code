#include <iostream>
#include <typeinfo>
#include <vector>
#include <algorithm>
using namespace std;

////////////////////////////////////////////////////////////////////////////////////////////////////
// right number comes -> 'append' to the end
// if middle number comes -> 'replace' the middle number 
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> dp;

        for (int num : nums) {

            // if num ==> largest, append
            if (dp.empty() || dp.back() < num) {
                dp.push_back(num);
            }

            // else, replace one element from the dp list
            else {
                auto it = lower_bound(dp.begin(), dp.end(), num);
                
                // *it => iterator가 가리키는 위치의 실제 값(int)
                // ex) 반환된 it가 dp[2]를 가리킨다면 *it은 dp[2]의 실제 값
                *it = num;
                }
        
        }
        // for (auto i = dp.begin(); i != dp.end(); ++i) {
        //     cout << *i << " ";
        // }
        // cout << endl;
        return dp.size();
    }
};
//////////////////////////////////////////////////////////////////
int main() {
    Solution solution;
    vector<int> nums = {10,9,2,5,3,7,101,18};
    int result = solution.lengthOfLIS(nums);
    cout << "Longest Increasing Subsequence: " << result << endl;
    // >>> 4
    // >>> (2,3,7,10)
    return 0;
}
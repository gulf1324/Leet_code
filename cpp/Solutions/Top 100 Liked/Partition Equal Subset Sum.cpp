#include <iostream>
#include <typeinfo>
#include <vector>
#include <numeric> //accumulate
using namespace std;

////////////////////////////////////////////////////////////////////////////////////////////////////
class Solution {
public:
    bool canPartition(const vector<int>& nums) {
        int totalSum = accumulate(nums.begin(), nums.end(), 0); // third argument is the initial value of the sum
        if (totalSum %2 != 0) {
            return false;
        }
        
        const int target = totalSum /2 ;
        size_t n = nums.size();

        vector<bool> dp(target+1, false); 
        dp[0] = true;

        for (int num : nums) {
            for (int i = target; i >= num; --i){
                dp[i] = dp[i] || dp[i-num];
            }
        }

    return dp[target];
    }
};
//////////////////////////////////////////////////////////////////
int main() {
    Solution solution;
    // vector<int> nums = {1,5,11,5};
    // >>> true
    // [1, 5, 5] == [11]
    vector<int> nums =  {1,2,3,5};
    // >>> false
    int result = solution.canPartition(nums);
    cout << "Partition Equal Subset Sum: " << result << endl;
    return 0;
}
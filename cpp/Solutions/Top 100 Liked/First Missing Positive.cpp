#include <iostream>
#include <typeinfo>
#include <vector>
#include <numeric> //accumulate
using namespace std;

////////////////////////////////////////////////////////////////////////////////////////////////////
// 1. map index
// 2. check index and return the corrected value
class Solution {
public: 
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size(); 
        
        // 1. reorder
        // ==> place each x at index x - 1 if 1 <= x <= n
        for (int i = 0; i < n; ++i) {
            while (nums[i] > 0 && 
                   nums[i] <= n && 
                   nums[nums[i] - 1] != nums[i]) {
                swap(nums[i], nums[nums[i] - 1]);
                }
            }
        
        // 2. pick the anomaly, correct it, and return
        for (int i = 0; i < n; ++i)
            if (nums[i] != i + 1)
                return i + 1;
        return n + 1; // ex) {1,2,3} ==> return 4
    }
};
////////////////////////////////////////////////////////////////////////////////////////////////////
int main() {
    Solution solution;
    vector<int> nums = {3,4,-1,1};
    int result = solution.firstMissingPositive(nums);
    cout << "first missing positive: " << result << endl;
    // >>> 2
    return 0;
}
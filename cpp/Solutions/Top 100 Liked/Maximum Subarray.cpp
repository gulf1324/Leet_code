#include <iostream>
#include <vector>
#include <algorithm> // For sort
using namespace std;

////////////////////////////////////////////////////////////////////////////////////////////////////
// Constraints : in-place, O(1)
// Time Limit Exceeded
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        while (k > 0) {
            nums.insert(nums.begin(), nums.back());
            nums.pop_back();
            k--;
        }
    }
};
////////////////////////////////////////////////////////////////////////////////////////////////////
// Kadane’s Algorithm ==> O(n)
class Solution {
public:
    int maxSubArray(std::vector<int>& nums) {
        int maxSum = nums[0];
        int currentSum = nums[0];
        
        for (size_t i = 1; i < nums.size(); ++i) {
            // Either extend the current subarray or start new from nums[i]
            currentSum = std::max(nums[i], currentSum + nums[i]);
            maxSum = std::max(maxSum, currentSum);
        }
        
        return maxSum;
    }
};
//////////////////////////////////////////////////////////////////
// Kadane’s Algorithm #2
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxi = INT_MIN;
        int sum = 0;

        for(int i = 0; i < nums.size(); i++) {
            sum = sum + nums[i];

            if(sum > maxi) {
                maxi = sum;
            }

            if(sum < 0) {
                sum = 0;
            }
        }

        return maxi;
    }
};
//////////////////////////////////////////////////////////////////
int main() {
    Solution solution;
    vector<int> nums = {-2,1,-3,4,-1,2,1,-5,4};
    int result = solution.maxSubArray(nums);
    cout << "Largest Sum:" << result <<endl;
    // >>> 6
    return 0;
}
#include <iostream>
#include <typeinfo>
#include <vector>
#include <numeric> //accumulate
using namespace std;

////////////////////////////////////////////////////////////////////////////////////////////////////
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int goal = nums.size() - 1;

        // check backwards
        for (int i = nums.size() - 2; i >= 0; i--) {
            if (i + nums[i] >= goal) {
                goal = i;
            }
        }

        // fail to reach the start 
        return goal == 0;        
    }
};
////////////////////////////////////////////////////////////////////////////////////////////////////
int main() {
    Solution solution;
    vector<int> nums = {2,3,1,1,4};
    bool result = solution.canJump(nums);
    cout << "Can jump to the end: " << result << endl;
    // >>> {9,7,8}
    return 0;
}
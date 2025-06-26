#include <iostream>
#include <typeinfo>
#include <vector>
using namespace std;

////////////////////////////////////////////////////////////////////////////////////////////////////
// Floyd's Tortoise and Hare (Cycle Detection)
// O(n), O(1)
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int slow = nums[0];
        int fast = nums[0];

        // 1단계: 싸이클 탐지 (Tortoise and Hare)
        // cpp do-while 문:
        // ==> do at least once before the while condition.
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);

        // 2단계: 사이클 입구 찾기 (중복 값)
        slow = nums[0];
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }

        return slow;
    }
};
//////////////////////////////////////////////////////////////////
int main() {
    Solution solution;
    vector<int> nums = {3,1,3,4,2};
    // >>> 2
    int result = solution.findDuplicate(nums);
    cout << "Duplicate number : " << result << endl;
    return 0;
}
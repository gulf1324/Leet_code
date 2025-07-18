#include <iostream>
#include <vector>
#include <algorithm> // For sort
#include <unordered_map> 
// ==> defaultdict(int)
using namespace std;

////////////////////////////////////////////////////////////////////////////////////////////////////
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> subNum;
        subNum[0] = 1;
        int total = 0, count = 0;

        for (int n : nums) {
            total += n;

            if (subNum.find(total - k) != subNum.end()) {
                count += subNum[total - k];
            }

            subNum[total]++;
        }

        return count;
    }
};
//////////////////////////////////////////////////////////////////
int main() {
    Solution solution;
    vector<int> nums = {1,1,1};
    int result = solution.subarraySum(nums, 2);
    cout << "Total number of subarrays: "<< result << endl;
    // >>> 2
    return 0;
}
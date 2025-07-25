#include <iostream>
#include <typeinfo>
#include <vector>
#include <algorithm> // for reverse, next_permutation

using namespace std;
//////////////////////////////////////////////////////////////////
// ex) 1,2,3 
// next ==> 1,3,2
// next ==> 2,1,3
// next ==> 2,3,1
// ...
// next ==> 3,2,1
// next ==> 1,2,3
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
    int n = nums.size();
    int i = n - 2;

    // 1) find first decreasing element from the right
    while (i >= 0 && nums[i] >= nums[i + 1]) --i;

    if (i >= 0) {
        // 2) find element just larger than nums[i] to the right
        int j = n - 1;
        while (nums[j] <= nums[i]) --j;
        swap(nums[i], nums[j]);
    }

    // 3) reverse the suffix
    reverse(nums.begin() + i + 1, nums.end());
    }
};
//////////////////////////////////////////////////////////////////
// using library
class Solution2 {
public:
void nextPermutation(vector<int>& nums) {
    next_permutation(nums.begin(), nums.end());
}
};
//////////////////////////////////////////////////////////////////
int main() {
    Solution solution;
    vector<int> nums = {1,2,4,3};
    // 1. i==1, nums[i] == 2
    // 2. j==3, nums[j] == 3 ==> swap ==> 1,3,4,2
    // 3. begin + i + 1 == 2
    // 3-1. reverse {1,3,2,4}
    solution.nextPermutation(nums);

    cout << "{" ;
    for (size_t i = 0; i < nums.size(); ++i) {
        if (i == 0) {
        cout << nums[i];
        } 
        else {
            cout << "," << nums[i];
        }
    }
    cout << "}" <<endl;
    // ==> 
    return 0;
}
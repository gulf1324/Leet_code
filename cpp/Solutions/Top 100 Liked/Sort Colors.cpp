#include <iostream>
#include <vector>
#include <algorithm> // For sort
// using namespace std; <== not good (?)

////////////////////////////////////////////////////////////////////////////////////////////////////
// Constraints : in-place/ O(n)/ O(1)
// **swap**
// Explanation
// https://loopccew.medium.com/dutch-national-flag-algorithm-91c469d9182b
class Solution {
public:
    void sortColors(std::vector<int>& nums) {
        int start = 0;                 // boundary for 0; beginnig of the array
        int i = 0;                   // current element
        int end = nums.size() - 1;  // boundary for 2; end of the array

        while (i <= end) {
            if (nums[i] == 0) {
                std::swap(nums[start], nums[i]);
                start++;
                i++;
            } else if (nums[i] == 1) {
                i++;
            } else {  // nums[i] == 2
                std::swap(nums[i], nums[end]);
                end--;
                // do not increment i here
            }
        }
    }
};
//////////////////////////////////////////////////////////////////
int main() {
    Solution solution;
    std::vector<int> nums = {2,0,2,1,1,0};
    solution.sortColors(nums);
    std::cout << "Sorted vector: {";
    
    for (size_t i = 0; i < nums.size(); ++i) {
        if (i == 0) {
        std::cout << nums[i];
        } 
        else {
            std::cout << "," << nums[i];
        }
    }
    std::cout << "}" <<std::endl;
    // >>> {0,0,1,1,2,2}
    return 0;
}
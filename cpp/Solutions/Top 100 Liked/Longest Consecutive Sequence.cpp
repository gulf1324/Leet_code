#include <iostream>
#include <typeinfo>
#include <vector>
#include <unordered_set>
#include <algorithm> // For max

//////////////////////////////////////////////////////////////////
class Solution {
public:
    int longestConsecutive(std::vector<int>& nums) {
        std::unordered_set<int> numSet(nums.begin(), nums.end());
        int longest = 0;

        for (int num : numSet) {
            // Python 
            // if (n - 1) not in num_set:
            if (numSet.find(num - 1) == numSet.end()) {
                int length = 1;

                while (numSet.find(num + length) != numSet.end()) {
                    length++;
                }

                longest = std::max(longest, length);
            }
        }

        return longest;
    }
};
//////////////////////////////////////////////////////////////////
int main() {
    std::vector<int> list1 = {100,4,200,1,3,2};
    // 4  ({1,2,3,4})
    Solution solution;
    int sorted = solution.longestConsecutive(list1);
    std::cout << "Longest Consecutive sequence: "<< sorted << std::endl;

    return 0;
}
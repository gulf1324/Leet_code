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
// Constraints : in-place, O(1)
// Reverse Algorithm
class Solution {
public:
    void rotate(std::vector<int>& nums, int k) {
        int n = nums.size();
        if (n == 0) {
            return;
        }

        // k를 배열의 크기로 나눈 나머지로 정규화
        // 이렇게 하면 k가 배열 크기보다 커도 올바르게 작동하며, 불필요한 회전을 방지
        k = k % n;

        // 1. 전체 배열을 뒤집기
        // **[7, 6, 5, 4, 3, 2, 1]**
        std::reverse(nums.begin(), nums.end());

        // 2. 처음부터 k개의 요소를 뒤집기
        // [** 5, 6, 7 **, 4, 3, 2, 1]
        std::reverse(nums.begin(), nums.begin() + k);

        // 3. 나머지 n - k개의 요소를 뒤집기
        // [5, 6, 7,** 1, 2, 3, 4**]
        std::reverse(nums.begin() + k, nums.end());
    }
};
//////////////////////////////////////////////////////////////////
int main() {
    Solution solution;
    vector<int> nums = {1,2,3,4,5,6,7};
    solution.rotate(nums, 3);
    cout << "Rotated vector: {";
    
    for (size_t i = 0; i < nums.size(); ++i) {
        if (i == 0) {
        cout << nums[i];
        } 
        else {
            cout << "," << nums[i];
        }
    }
    cout << "}" <<endl;
    // >>> {5,6,7,1,2,3,4}
    return 0;
}
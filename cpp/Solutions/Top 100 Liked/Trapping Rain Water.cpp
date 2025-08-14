#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm> // For sort
using namespace std;

////////////////////////////////////////////////////////////////////////////////////////////////////
class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() <= 2) return 0;
        
        int n = height.size(), maxLeft = height[0], maxRight = height[n-1];
        int left = 1, right = n - 2, ans = 0;
        
        while (left <= right) {
            
            // if left is the tallest, start from left
            if (maxLeft < maxRight) {
                if (height[left] > maxLeft)
                    maxLeft = height[left];
                else
                    ans += maxLeft - height[left];
                left += 1;
            } 
            // if right is the tallest, start from right
            else {
                if (height[right] > maxRight)
                    maxRight = height[right];
                else
                    ans += maxRight - height[right];
                right -= 1;
            }
        }
        
        return ans;
    }
};
//////////////////////////////////////////////////////////////////
int main() {
    Solution solution;
    vector<int> height = {0,1,0,2,1,0,1,3,2,1,2,1};
    int result = solution.trap(height);
    cout << result << endl;
    return 0;
}
#include <iostream>
#include <typeinfo>
#include "../../Learn C++/LinkedList.h"
#include <unordered_map>
#include <vector>
#include <deque>
using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> result;
        deque<int> dq; 
        
        for (int i = 0; i < nums.size(); i++) {
            // 윈도우 범위를 벗어난 인덱스 제거
            if (!dq.empty() && dq.front() < i - k + 1) {
                dq.pop_front(); // could only be single element, thus if <-> while (O)
            }
            
            // 현재 원소보다 작은 원소들의 인덱스를 뒤에서부터 제거
            while (!dq.empty() && nums[dq.back()] < nums[i]) {
                dq.pop_back(); // could be multiple elements, thus only while (O)
            }
            
            // 현재 인덱스 추가
            dq.push_back(i);
            
            // 윈도우 크기가 k에 도달하면 최댓값 추가
            if (i >= k - 1) {
                result.push_back(nums[dq.front()]);
            }
        }
        
        return result;
    }
};
//////////////////////////////////////////////////////////////////
int main() {
    Solution solution;
    
    vector<int> nums = {1,3,-1,-3,5,3,6,7};
    int k = 3;
    vector<int> result = solution.maxSlidingWindow(nums, k);
    for (size_t i = 0; i < result.size(); i++)
    {
        cout<< result[i] << endl;
    }
    


    return 0;
}
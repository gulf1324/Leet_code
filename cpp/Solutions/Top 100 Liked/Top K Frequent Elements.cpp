#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

////////////////////////////////////////////////////////////////////////////////////////////////////
// Constraints : 
// k is in the range [1, the number of unique elements in the array].
// The algorithm's time complexity must be better than O(n log n), where n is the array's size.
// Using 'bucket sort'
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counter;
        for (int n : nums) {
            counter[n]++;
        }
        
        vector<vector<int>> freq(nums.size() + 1);
        for (auto& entry : counter) {
            freq[entry.second].push_back(entry.first);
            // freq[count value as an index].append(actual number)
            // freq = {  { }
            //           { 3 }   
            //           { 2 }
            //           { 1 }
            //           { }
            //           { }
            //           { } };          
        }
        
        vector<int> res;
        for (int i = freq.size() - 1; i >= 0; i--) {
            for (int num : freq[i]) {
                res.push_back(num);
                if (res.size() == k) {
                    return res;
                }
            }
        }
        
        return {};        
    }
};
/////////////////////////////////////////////////////////////////
int main() {
    Solution solution;
    vector<int> nums = {1,1,1,2,2,3};
    int k = 2;
    vector<int> result = solution.topKFrequent(nums, k);
    
    cout << "Top K elements : {";
    
    for (size_t i = 0; i < result.size(); ++i) {
        if (i == 0) {
        cout << result[i];
        } 
        else {
            cout << "," << result[i];
        }
    }
    cout << "}" <<endl;
    
    // {1,2}
    return 0;
}
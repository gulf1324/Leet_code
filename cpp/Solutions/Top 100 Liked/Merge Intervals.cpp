#include <iostream>
#include <vector>
#include <algorithm> // For sort
#include <algorithm>
using namespace std;

////////////////////////////////////////////////////////////////////////////////////////////////////
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.empty() || intervals.size() == 1) {
            return intervals;
        }

        // 1. sort 
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0]; // Sort by first element
        });

        vector<vector<int>> res;
        
        // Add the first interval to our result list as a starting point.
        res.push_back(intervals[0]);

        // 2. Iterate through the sorted intervals starting from the second one.
        for (size_t i = 1; i < intervals.size(); ++i) {
            
            // last element of res 
            vector<int>& lastMerged = res.back();
            // current element of input vector
            const vector<int>& current = intervals[i];

            // Check for overlap:
            // An overlap occurs if the start of the current interval is less than or
            // equal to the end of the last merged interval.
            if (current[0] <= lastMerged[1]) {
                // Overlap exists, so merge them.
                // Update the end of the last merged interval to be the maximum of
                // its current end and the current interval's end.
                lastMerged[1] = max(lastMerged[1], current[1]);
            } else {
                // No overlap, so add the current interval as a new, separate merged interval.
                res.push_back(current);
            }
        }
        return res;
    }
};
//////////////////////////////////////////////////////////////////
int main() {
    Solution solution;
    vector<vector<int>> intervals = {{1,3},{2,6},{8,10},{15,18}};
    vector<vector<int>> result = solution.merge(intervals);
    cout << "Merged intervals: ";
    
    for (const auto& interval : result) {
        cout << "{" << interval[0] << "," << interval[1] << "} ";
    }
    cout << endl;
    // >>> {{1,6}, {8,10}, {15,18}}
    return 0;
}
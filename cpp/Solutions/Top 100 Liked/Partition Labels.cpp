#include <iostream>
#include <typeinfo>
#include <vector>
#include <numeric> //accumulate
using namespace std;

////////////////////////////////////////////////////////////////////////////////////////////////////
class Solution {
public:
    vector<int> partitionLabels(string s) {
        
        vector<int> lastIndex(26, -1);
        for (int i = 0; i < s.size(); ++i) {
            lastIndex[s[i] - 'a'] = i;
        }

        cout << "{";
        for (int i:lastIndex) {
            cout << i << ", " ;
        }
        cout << "}" << endl;
        // ex)  "abca"
        // lastIndex == {3, 1, 2, -1, ... ,-1}
        // ==> last index that character appreared in the string

        vector<int> result;
        int start = 0, end = 0;


        for (int i = 0; i < s.size(); ++i) {
            // first, set end immediately to the last index of the current character
            end = max(end, lastIndex[s[i] - 'a']);
            if (i == end) {
                // partition complete, append the size of the partition
                result.push_back(end - start + 1);
                start = end + 1;
            }
        }

        return result;
    }
};
////////////////////////////////////////////////////////////////////////////////////////////////////
int main() {
    Solution solution;
    string s = "ababcbacadefegdehijhklij";
    vector<int> result = solution.partitionLabels(s);
    cout << "Partition lengths: " << endl;
    
    for (int i:result) {
        cout << i << endl;
    }
    // >>> {9,7,8}
    return 0;
}
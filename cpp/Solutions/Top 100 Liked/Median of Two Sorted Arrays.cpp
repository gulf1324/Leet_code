#include <iostream>
#include <vector>
#include "../../Learn C++/Tree.h"

using namespace std;
//////////////////////////////////////////////////////////////////////////////////////////
// the two vectors are sorted
// linear
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        int m = nums2.size();
        int i = 0, j = 0, m1 = 0, m2 = 0;

        // Find median.
        for (int count = 0; count <= (n + m) / 2; ++count) {
            // m2 ==> previous value
            // m1 ==> current value
            m2 = m1;
            
            // if (i < n && j < m) 
            // ==> both within range
            if (i != n && j != m) { 
                if (nums1[i] > nums2[j]) {
                    m1 = nums2[j++];
                } 
                else { // (nums1[i] <= nums2[j])
                    m1 = nums1[i++];
                }
            } 
            
            // else if (i < n && j >= m)
            // ==> only nums1 within range
            else if (i < n) { 
                m1 = nums1[i++];
            } 
            
            // else if (i >= n && j < m)
            // ==> only nums2 within range
            else {
                m1 = nums2[j++];
            }
        }

        // Check if the sum of n and m is odd.
        if ((n + m) % 2 == 1) {
            return static_cast<double>(m1);
        } else {
            double ans = static_cast<double>(m1) + static_cast<double>(m2);
            return ans / 2.0;
        }
    }
};
//////////////////////////////////////////////////////////////////////////////////////////
int main() {
    std::vector<int> vector1 = {1, 2};
    std::vector<int> vector2 = {3, 4};
    Solution solution;
    
    double res = solution.findMedianSortedArrays(vector1, vector2);
    cout << res << endl;
    // 2.50000

    return 0;
}
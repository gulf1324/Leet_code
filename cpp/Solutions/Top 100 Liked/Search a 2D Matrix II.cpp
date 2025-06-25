#include <iostream>
#include <typeinfo>
#include <vector>
using namespace std;

////////////////////////////////////////////////////////////////////////////////////////////////////
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
    if (matrix.empty() || matrix[0].empty()) return false;
    
    int m = matrix.size();
    int n = matrix[0].size();
    int row = 0;
    int col = n - 1;
    
    int loop = 0;
    while (row < m && col >= 0) {
        // cout << loop++ << ", " << matrix[row][col] << endl;
        // 0, 15
        // 1, 11
        // 2, 7
        // 3, 4
        // 4, 5
        
        if (matrix[row][col] == target) {
            return true;
        } else if (matrix[row][col] > target) {
            col--;
        } else {
            row++;
        }
    }
    
    return false;
    }
};

//////////////////////////////////////////////////////////////////
int main() {
    Solution solution;
    vector<vector<int>> matrix = {{1,  4,  7,  11, 15},
                                  {2,  5,  8,  12, 19}, 
                                  {3,  6,  9,  16, 22}, 
                                  {10, 13, 14, 17, 24}, 
                                  {18, 21, 23, 26, 30}};
    // >>> true
    int result = solution.searchMatrix(matrix, 5);
    cout << "Is target in matrix: " << result << endl;
    return 0;
}
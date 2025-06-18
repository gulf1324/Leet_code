#include <iostream>
#include <typeinfo>
#include <vector>
using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size(); 

        vector<vector<int>> dp(m, vector<int>(n, grid[0][0]));
        
        // for (const auto& row : dp) {
        //     for (const auto& val : row) {
        //         cout << val << " ";
        //     }
        //     cout << endl;
        // }
        // 1 1 1
        // 1 1 1
        // 1 1 1

        // initialize first row
        for (int j = 1; j < n; ++j)
            dp[0][j] = dp[0][j - 1] + grid[0][j];
        
        // initialize first column
        for (int i = 1; i < m; ++i)
            dp[i][0] = dp[i - 1][0] + grid[i][0];
        
        // fill the rest grid
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                dp[i][j]  = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j];
            }
        }
        
        // for (const auto& row : dp) {
        //     for (const auto& val : row) {
        //         cout << val << " ";
        //     }
        //     cout << endl;
        // }
        
        // 1 4 5
        // 2 7 6
        // 6 8 7

        return dp[m - 1][n - 1];
    }
};
//////////////////////////////////////////////////////////////////
int main() {
    Solution solution;
    vector<vector<int>> grid = {{1,3,1},{1,5,1},{4,2,1}};
    int result = solution.minPathSum(grid);
    cout << "Longest valid parentheses length: " << result << endl;
    return 0;
}
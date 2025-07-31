#include <iostream>
#include <typeinfo>
#include <vector>
using namespace std;

////////////////////////////////////////////////////////////////////////////////////////////////////
class Solution {
public:
    void dfs(vector<vector<char>>& grid, int i, int j) {
        int m = grid.size();
        int n = grid[0].size();

        // Boundary or already visited('0') check
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == '0') {
            return;
            }

        // Mark current land as visited
        grid[i][j] = '0';

        // Visit 4 directions
        dfs(grid, i + 1, j); // down
        dfs(grid, i - 1, j); // up
        dfs(grid, i, j + 1); // right
        dfs(grid, i, j - 1); // left
    }

    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()) return 0;

        int m = grid.size();
        int n = grid[0].size();
        int islands = 0;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == '1') {
                    dfs(grid, i, j); // checks all possible grids and mark it as 0s. 
                    ++islands;
                }
            }
        }

        return islands;
    }
};
//////////////////////////////////////////////////////////////////
int main() {
    Solution solution;
    vector<vector<char>> matrix = {{'1','1','0','0','0'},
                                   {'1','1','0','0','0'},
                                   {'0','0','1','0','0'},
                                   {'0','0','0','1','1'}};
                                
                                // "essential" grid
                                // {{'1','0','0','0','0'},
                                //  {'0','0','0','0','0'},
                                //  {'0','0','1','0','0'},
                                //  {'0','0','0','1','0'}}

    int result = solution.numIslands(matrix);
    cout << "Number of islands: " << result << endl;
    return 0;
}
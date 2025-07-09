#include <iostream>
#include <vector>
#include <algorithm> 
using namespace std;

////////////////////////////////////////////////////////////////////////////////////////////////////
// Constraints : -100 <= matrix[i][j] <= 100
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        int x = 0;
        int y = 0;
        int dx = 1;
        int dy = 0;
        vector<int> res;

        // for number-of-elements times in matrix
        for (int i = 0; i < rows * cols; ++i) {
            res.push_back(matrix[y][x]);
            
            // mark as visited
            matrix[y][x] = -101;

            // if next step is not in bound or visited {change direction}
            if (!(0 <= x + dx && x + dx < cols && 0 <= y + dy && y + dy < rows) || matrix[y+dy][x+dx] == -101) {
                int temp = dx;
                dx = -dy;
                dy = temp;
                //     →   ↓   ←   ↑  |  →   ↓
                // dx  1   0  -1   0  |  1   0 ...
                // dy  0   1   0  -1  |  0   1 ...
            }

            x += dx;
            y += dy;
        }

        return res;
    }        
};
//////////////////////////////////////////////////////////////////
int main() {
    Solution solution;
    vector<vector<int>> matrix = {{1,2,3},{4,5,6},{7,8,9}};
    vector<int> result = solution.spiralOrder(matrix);
    cout << "Spiral-ed order : {";
    
    for (size_t i = 0; i < result.size(); ++i) {
        if (i == 0) {
        cout << result[i];
        } 
        else {
            cout << "," << result[i];
        }
    }
    cout << "}" <<endl;
    // >>> {1,2,3,6,9,8,7,4,5}
    return 0;
}
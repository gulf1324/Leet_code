#include <iostream>
#include <typeinfo>
#include <vector>
#include <stack>
using namespace std;

// for debugging
void printStep(const vector<int>& heights, int i, const stack<int>& st, int area = -1) {
    cout << "i=" << i;
    if (i < heights.size()) cout << " (높이=" << heights[i] << ")";
    
    cout << " 스택: [";
    stack<int> temp = st;
    vector<int> elements;
    while (!temp.empty()) {
        elements.push_back(temp.top());
        temp.pop();
    }
    for (int j = elements.size() - 1; j >= 0; j--) {
        cout << elements[j];
        if (j > 0) cout << ", ";
    }
    cout << "]";
    
    if (area != -1) {
        cout << " → 계산된 넓이: " << area;
    }
    cout << endl;
}


class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int> indexStack;  // save index
        int maxArea = 0;
        int n = heights.size();
        
        for (int i = 0; i <= n; ++i) {
            // 마지막에 0을 추가한 것처럼 처리 (모든 막대 처리 보장)
            int currentHeight = (i == n) ? 0 : heights[i];
            printStep(heights, i, indexStack);
            
            // 현재 높이가 스택 맨 위보다 작으면 계산 시작
            while (!indexStack.empty() && heights[indexStack.top()] > currentHeight) {
                int top = indexStack.top();
                indexStack.pop();
                
                // 넓이 계산: 
                // - 스택이 비어있으면 처음부터 현재까지
                // - 아니면 (현재 인덱스 - 스택 맨 위 - 1)
                int width = indexStack.empty() ? i : i - indexStack.top() - 1;
                
                int area = heights[top] * width;
                maxArea = max(maxArea, area);

                // ex) [0,1,2]  i == 3
                //      → [0,1]  5*1 => maxArea = 5
                //      → [0]  4*2 => maxArea = 8
                //      → []  2*3 => maxArea = 6
                printStep(heights, i, indexStack, area);
            }
            
            indexStack.push(i);
        }
        
        return maxArea;
    }
};
//////////////////////////////////////////////////////////////////////////////////////////////////
int main() {
    Solution solution;

    int numCourses = 4;
    vector<int> heights = {2,4,5,1,2,3};
    // ==> 10
    
    int result = solution.largestRectangleArea(heights);

    cout << result << endl;

    return 0;
}
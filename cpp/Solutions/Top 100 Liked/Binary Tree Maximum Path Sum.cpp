#include <iostream>
#include <typeinfo>
#include <vector>
#include "../../Learn C++/Tree.h"

using namespace std;

////////////////////////////////////////////////////////////////////////////////////////////////////
class Solution {
    int maxSum;
public:
    int maxPathSum(TreeNode* root) {
        maxSum = INT_MIN;
        dfs(root);
        return maxSum;
    }

private:
    int dfs(TreeNode* node) {
        if (!node) return 0;
        
        // 왼쪽과 오른쪽 서브트리에서의 최대 경로 합
        // 음수인 경우 0으로 처리 (해당 경로를 선택하지 않음)
        int leftMax = max(0, dfs(node->left));
        int rightMax = max(0, dfs(node->right));
        
        // 현재 노드를 지나는 경로의 최대 합
        // (왼쪽 경로 + 현재 노드 + 오른쪽 경로)
        // ==> "수평적 경로일 경우 최댓값"
        int currentPathSum = node->val + leftMax + rightMax;
        maxSum = max(maxSum, currentPathSum);
        
        // 상위 노드로 반환할 값: 현재 노드 + 왼쪽 또는 오른쪽 중 더 큰 값
        // ==> "수직적 경로일 경우 최댓값"
        return node->val + max(leftMax, rightMax);
    }
};
//////////////////////////////////////////////////////////////////
void printInorder(TreeNode* node) {
    if (node) {
        printInorder(node->left);
        cout << node->val << " ";
        printInorder(node->right);
    }
}

int main() {
    Solution solution;

    //      -10
    //      /  \
    //     9   20
    //        /  \
    //       15   7
    // ==> 15 → 20 → 7
    // 42
    TreeNode* root = new TreeNode(-10);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left = new TreeNode(15);
    root->right->right = new TreeNode(7);

    printInorder(root);
    cout << endl;
    int result = solution.maxPathSum(root);
    cout << "Max sum path: " << result << endl;
    return 0;
}
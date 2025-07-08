#include <iostream>
#include <vector>
#include <stack>
#include "../../Learn C++/Tree.h"
using namespace std;

////////////////////////////////////////////////////////////////////////////////////////////////////
// Constraints : 
//      BST
//      1 <= k <= n <= 10^4
//      0 <= Node.val <= 10^4
// Recursive
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        int count = 0;
        int result = -1;
        inOrder(root, k, count, result);
        return result;
    }

private:
    void inOrder(TreeNode *node, int k, int count, int result) {
        if (!node) return;

        inOrder(node->left, k, count, result);

        count++;
        if (count == k) {
            result = node->val;
            return;
        }

        inOrder(node->right, k, count, result);
    }
};
////////////////////////////////////////////////////////////////////////////////////////////////////
// Iterative stack
class Solution2 {
public:
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> stk;
        TreeNode* curr = root;

        while (curr || !stk.empty()) {
            
            // add all lefts to stack
            while (curr) {
                stk.push(curr);
                curr = curr->left;
            }

            // stk.top() ==> most recently pushed element ==> **the smallest**
            //      stk.pop() -> None
            curr = stk.top();
            stk.pop();

            // do it k times
            k--;
            if (k == 0) return curr->val;

            // "check" if right exists;
            //      if there is, added to stack due to while (curr)
            //      if none, go on to next 'lefts' in the stack
            curr = curr->right;
        }

        return -1;
    }
};
////////////////////////////////////////////////////////////////////////////////////////////////////
int main() {
    Solution2 solution;
    TreeNode *root = new TreeNode(5);
    root->left = new TreeNode(3);
    root->right = new TreeNode(6);
    
    root->left->left = new TreeNode(2);
    root->left->right = new TreeNode(4);
    
    root->left->left->left = new TreeNode(1);
    
    //        5
    //       / \
    //      3   6
    //     / \     
    //    2   4     
    //   /
    //  1

    int result = solution.kthSmallest(root, 3);
    cout << "Kth smallest value: "<< result << endl;
    // >>> 3
    return 0;
}
#include <iostream>
#include <queue>
#include <vector>
#include <unordered_map>
#include <string>
#include "../../Learn C++/Tree.h"

using namespace std;

class Solution {
public:
    unordered_map<int, int> mp;

    TreeNode* construct(vector<int>& preorder, vector<int>& inorder, int l, int r, int& idx) {
        if(l > r)
            return NULL;
        
        int rootVal = preorder[idx];
        idx++;
        int i = mp[rootVal];
        
        TreeNode* root = new TreeNode(rootVal);
        root->left = construct(preorder, inorder, l, i-1, idx);
        root->right = construct(preorder, inorder, i+1, r, idx);
        
        return root;
    }
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        mp.clear();
        int n = preorder.size();
        for(int i = 0; i<n; i++) {
            mp[inorder[i]] = i;
        }
        
        int idx = 0;
        return construct(preorder, inorder, 0, n-1, idx);
    }
};

void printBFS(TreeNode* root) {
    if (!root) {
        cout << "null\n";
        return;
    }

    queue<TreeNode*> q;
    vector<string> result;

    q.push(root);

    while (!q.empty()) {
        TreeNode* node = q.front();
        q.pop();

        if (node) {
            result.push_back(to_string(node->val));
            q.push(node->left);
            q.push(node->right);
        } else {
            result.push_back("null");
        }
    }

    while (!result.empty() && result.back() == "null") {
        result.pop_back();
    }

    for (const string& val : result) {
        cout << val << " ";
    }
    cout << endl;
}
//////////////////////////////////////////////////////////////////
int main() {
    std::vector<int> preorder = {3,9,20,15,7};
    std::vector<int> inorder = {9,3,15,20,7};
    Solution solution;
    TreeNode* res = solution.buildTree(preorder, inorder);

    printBFS(res);
    // 3 9 20 null null 15 7

    return 0;
}
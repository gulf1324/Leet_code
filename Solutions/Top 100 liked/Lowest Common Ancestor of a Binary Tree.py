from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: 
                node.left = kids.pop()
            if kids: 
                node.right = kids.pop()
    return root
##################################################################################
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root 
        left = self.lowestCommonAncestor(root.left, p, q)  
        right = self.lowestCommonAncestor(root.right, p, q)  

        if left and right:
            return root 
        return left if left else right 
##################################################################################    
root = build_tree(root = [3,5,1,6,2,0,8,None,None,7,4])
s = Solution()
print(s.lowestCommonAncestor(root, p = 5, q = 1))
# >>> 3
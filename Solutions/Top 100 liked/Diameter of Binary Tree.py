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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            self.max_diameter = max(self.max_diameter, left + right)

            return max(left, right) + 1

        dfs(root)
        return self.max_diameter
##################################################################################    
root = build_tree(root = [1,2,3,4,5])
s = Solution()
print(s.diameterOfBinaryTree(root))
# >>> 3
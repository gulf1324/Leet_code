# Definition for a binary tree node.
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
    """
    These objects are not assigned to specific variable names like node_1 = TreeNode().
    Instead, they exist as anonymous objects within the nodes list.
    Each object is fully functional and can be accessed or manipulated 
    via its position in the list. ex) nodes[0].val
    
    This approach is memory-efficient and avoids explicitly declaring 
    variables for each node, especially for large trees.
    """
    
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: 
                node.left = kids.pop()
            if kids: 
                node.right = kids.pop()
    return root

################################################################################
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))
################################################################################

root = build_tree([3, 9, 20, None, None, 15, 7])
s = Solution()
print("Maximum Depth:", s.maxDepth(root))
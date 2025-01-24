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
from collections import deque
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.collect_leaves_dfs(root1, []) == self.collect_leaves_dfs(root2, [])
        
        # print(f"{self.collect_leaves_bfs(root1)}\n{self.collect_leaves_bfs(root2)}")
        # return self.collect_leaves_bfs(root1) == self.collect_leaves_bfs(root2)
        # >>> Wrong, bfs return depth-wise left-to-right order of leaves
    
    def collect_leaves_dfs(self, node, leaves):
        if not node:
            return 
        if not node.left and not node.right: 
            leaves.append(node.val)
        else:
            self.collect_leaves_dfs(node.left, leaves)
            self.collect_leaves_dfs(node.right, leaves)
        return leaves
    
    def collect_leaves_bfs(self, root):
        if not root:
            return []
        leaves = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node.left and not node.right:
                leaves.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return leaves
################################################################################

root1 = build_tree([3,5,1,6,2,9,8,None,None,7,4])
root2 = build_tree([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])
s = Solution()
print("Leaf the same:", s.leafSimilar(root1, root2))
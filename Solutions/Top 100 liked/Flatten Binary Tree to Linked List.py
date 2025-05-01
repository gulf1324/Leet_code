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

from typing import Optional
from collections import deque
################################################################################################
# Wrong
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return []
        tmp = deque([])
        
        def dfs(node):
            tmp.append(node.val if node else None)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        
        dfs(root)
        tmp.popleft()
        print(tmp)
        while tmp:
            node_right = tmp.popleft()
            root.right = node_right
################################################################################################
# recursion DFS
class Solution:
    head = None
    def flatten(self, root: TreeNode) -> None:
        def revPreOrder(node: TreeNode) -> None:
            if node.right: 
                revPreOrder(node.right)
            if node.left: 
                revPreOrder(node.left)
            
            node.left = None
            node.right = self.head
            self.head = node

        if root: 
            revPreOrder(root)
################################################################################################        
s = Solution()
# root = build_tree([2,1,3])
# print(s.isValidBST(root))
# # >>> True

# root = build_tree([5,1,4,None,None,3,6])
# print(s.isValidBST(root))
# # >>> False

root = build_tree([1,2,5,3,4,None,6])
print(s.flatten(root))
# >>> [1,None,2,None,3,None,4,None,5,None,6]
# >>> 
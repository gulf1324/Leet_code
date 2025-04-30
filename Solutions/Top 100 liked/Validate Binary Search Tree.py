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
# Failed (30 minutes)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        stack = deque([root])
        min_root = root.val
        while stack:
            node = stack.popleft()
            min_root = min(node.val, min_root)
        
            if node.left:
                if node.left.val < node.val and node.left.val > min_root:
                    stack.append(node.left)
                else:
                    return False
            if node.right:
                if node.right.val > node.val and node.right.val < min_root:
                    stack.append(node.right)
                else:
                    return False
        
        return True
################################################################################################
# DFS recursion
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))
        
        return validate(root)
################################################################################################
# DFS Iterative
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = [(root, float('-inf'), float('inf'))]

        while queue:
            node, low, high = queue.pop()
            
            if not (low < node.val < high):
                return False

            if node.left:
                queue.append((node.left, low, node.val))  
            if node.right:
                queue.append((node.right, node.val, high))

        return True
################################################################################################    
# BFS Iterative
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # (node, min_bound, max_bound)
        queue = deque([(root, float('-inf'), float('inf'))])

        while queue:
            node, low, high = queue.popleft()
            
            if not (low < node.val < high):
                return False

            if node.left:
                queue.append((node.left, low, node.val))   
            if node.right:
                queue.append((node.right, node.val, high)) 

        return True
################################################################################################    
s = Solution()
# root = build_tree([2,1,3])
# print(s.isValidBST(root))
# # >>> True

# root = build_tree([5,1,4,None,None,3,6])
# print(s.isValidBST(root))
# # >>> False

root = build_tree([5,4,6,None,None,3,7])
print(s.isValidBST(root))
# >>> False
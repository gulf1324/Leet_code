from typing import Optional
from collections import deque
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
def print_inorder(root):
    stack = deque([root])
    res = []
    while stack:
        for _ in range(len(stack)):
            node = stack.popleft()
            res.append(node)
            if not node:
                continue
            if node.left or node.right:
                stack.append(node.left)
                stack.append(node.right)
    print([i.val if i != None else None for i in res])
##########################################################################################
# BFS
# 12 minutes
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    node.left, node.right = node.right, node.left
        return root
##########################################################################################
# more efficient BFS
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)    
        return root
##########################################################################################    
# DFS
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root
##########################################################################################    
s = Solution()
root = build_tree([4,2,7,1,3,6,9])
print_inorder(s.invertTree(root))
# >>> [4,7,2,9,6,3,1]

root = build_tree([2,1,3])
print_inorder(s.invertTree(root))
# >>> [2,3,1]

        
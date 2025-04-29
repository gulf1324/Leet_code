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
##############################################################################################################################
# BFS(solved before)
# 17 minutes, passed (100%/88%)
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        
        queue = deque([root])
        res = []
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(node.val)
        return res
##############################################################################################################################
root = build_tree([1,2,3,None,5,None,4])
s = Solution()
print(s.rightSideView(root))
# >>> [1,3,4]
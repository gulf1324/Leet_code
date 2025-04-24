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
#####################################################################################
# My solution (iterative BFS)
# 12 minutes, passed (100%/87%)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    tmp.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if tmp:
                res.append(tmp)
        return res
#####################################################################################        
root = build_tree([3,9,20,None,None,15,7])
s = Solution()
print(s.levelOrder(root))
# >>> [[3],[9,20],[15,7]]
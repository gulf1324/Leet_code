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
##############################################################################################################
# My solution (iterative BFS)
# 22 minutes, passed (100%/84%)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        while queue:
            if all(item is None for item in queue):
                return True
            
            level = [node.val if node else None for node in queue]
            if level != level[::-1]:
                return False
            
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    # enqueues "level-wise"
                    queue.append(node.left)
                    queue.append(node.right)
        return True
##############################################################################################################
# More readable
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        queue = deque([(root.left, root.right)])
        while queue:
            t1, t2 = queue.popleft()
            if not t1 and not t2:
                continue
            if not t1 or not t2 or t1.val != t2.val:
                return False
            
            # enqueues from "end pairs" to "middle pairs"
            queue.append((t1.left, t2.right))
            queue.append((t1.right, t2.left))

        return True
##############################################################################################################    
s = Solution()
root = build_tree([1,2,2,3,4,4,3])
print(s.isSymmetric(root))
# >>> True

root = build_tree([1,2,2,None,3,None,3])
print(s.isSymmetric(root))
# >>> False
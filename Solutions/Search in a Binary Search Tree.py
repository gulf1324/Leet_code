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
##########################################################################################################
# Returning a whole list of subtree
class Solution1:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        queue = deque([root])
        found_queue = deque([])
        res = []
        found = False
        while not found:
            node = queue.popleft()
            if node.val == val:
                found_queue.append(node)
                found = True
            else:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        while found and found_queue:
            node = found_queue.popleft()
            res.append(node)
            if node.left:
                found_queue.append(node.left)
            if node.right:
                found_queue.append(node.right)

        return res
##########################################################################################################
# Return the target node else None (slow runtime)
class Solution2:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        res = None
        while queue:
            node = queue.popleft()
            if node.val == val:
                res = node
                return res
            else:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return None
##########################################################################################################
# return the target node DFS (random search)
class Solution3:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        return self.searchBST(root.left, val) or self.searchBST(root.right, val)
##########################################################################################################
# knowing it's a BST(Binary Search Tree)
"""
Binary Search Tree
1. Left Subtree Property: All nodes in the left subtree have values less than the current node.
2. Right Subtree Property: All nodes in the right subtree have values greater than the current node.
3. No Duplicates: Typically, BSTs do not contain duplicate values.
"""
class Solution4:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        return self.searchBST(root.left, val) if root.val > val else self.searchBST(root.right, val)
##########################################################################################################
root = build_tree([4,2,7,1,3])
s = Solution4()
a = s.searchBST(root = root, val = 7)
print("Target node:", a)
print("Target node val :", (a.val if a else None))
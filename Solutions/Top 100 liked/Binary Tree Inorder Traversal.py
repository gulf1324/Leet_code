from typing import Optional

# Definition for a binary tree node.
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
##########################################################################################
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
##########################################################################################
# more readable
class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        stack = []
        node = root 

        while node or stack:
            # as far left as possible, appending each to stack
            while node:
                stack.append(node)
                node = node.left

            # if no child on left,
            #  1. append the stack's last node's val to res
            #  2. try the last node's right path
            node = stack.pop()
            res.append(node.val)
            node = node.right

        return res
##########################################################################################
root = build_tree([1,2,3,4,5,None,8,None,None,6,7,9])

s = Solution2()
print(s.inorderTraversal(root))
# >>> [4,2,6,5,7,1,3,9,8]
        
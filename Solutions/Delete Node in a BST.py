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
class Solution:
    # test
    def dfs(self, root)-> list[int]:
        res = []
        node = root
        res.append(node.val)
        if node.left:
            res += self.dfs(node.left)
        if node.right:
            res += self.dfs(node.right)
        return res
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        # Step 2: Found the node to delete
        else: 
            
            # Case 1: Node has no children (leaf node) or one child
            if not root.left:
                return root.right  # Return right child (could be None)
            elif not root.right:
                return root.left  # Return left child (could be None)
            
            # Case 2: Node has two children
            successor = self.getMin(root.right)
            root.val = successor.val  # Replace value
            root.right = self.deleteNode(root.right, successor.val)

        return root

    def getMin(self, node: TreeNode) -> TreeNode:
        """Finds the smallest value in the right subtree (inorder successor)."""
        while node.left:
            node = node.left
        return node
##########################################################################################################
root = build_tree([5,3,6,2,4,None,7])
s = Solution()
a = s.deleteNode(root, 3)
print("Deleted-node Tree:", s.dfs(a))
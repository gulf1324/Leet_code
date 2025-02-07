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
from typing import Optional
#################################################################################################################
# recursive
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.longest_so_far = 0 
        
        def dfs(node, direction, length) -> int:
            if not node:
                return 0
            self.longest_so_far = max(self.longest_so_far, length)

            # if the taken node's move was left try moving right
            if direction == 0: 
                dfs(node.left, 1, length + 1)  # switch next node's direction to right
                dfs(node.right, 0, 1)  # Restart ZigZag from right
            
            # if the taken node's move was right try moving left
            else:
                dfs(node.right, 0, length + 1)  # switch next node's direction to left
                dfs(node.left, 1, 1)  # Restart ZigZag from left

            return length
        
        # Start dfs from root in both left and right directions
        dfs(root.left, 1, 1)  # Move left first
        dfs(root.right, 0, 1)  # Move right first

        return self.longest_so_far
#################################################################################################################
# iterative
from collections import deque
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        max_length = 0
        stack = deque([(root, 0, 0), (root, 1, 0)])  # (node, direction, length)

        while stack:
            node, direction, length = stack.pop()
            max_length = max(max_length, length)

            if direction == 0 and node.left:  # Moving left
                stack.append((node.left, 1, length + 1))  # Change to right
                stack.append((node.left, 0, 0))  # Restart if continuing left
            
            if direction == 1 and node.right:  # Moving right
                stack.append((node.right, 0, length + 1))  # Change to left
                stack.append((node.right, 1, 0))  # Restart if continuing right
        
        return max_length
#################################################################################################################

# test case #1
root = build_tree([1,None,1,1,1,None,None,1,1,None,1,None,None,None,1])
s = Solution()
print("Max zigzag paths:", s.longestZigZag(root))
# >>> 3

# test case #2
root = build_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])
s = Solution()
print("Max zigzag paths:", s.longestZigZag(root))
# >>> 3
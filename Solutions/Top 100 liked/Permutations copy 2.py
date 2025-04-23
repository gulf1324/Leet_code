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

from collections import deque

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
# recursive
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root
##########################################################################################
# iterative
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        stack = []
        n = len(nums)
        
        mid = n // 2
        root = TreeNode(nums[mid])
        
        # Push root and its left and right subtree ranges
        stack.append((root, 0, mid - 1, mid + 1, n - 1))
        
        while stack:
            node, left_start, left_end, right_start, right_end = stack.pop()
            
            # Process left subtree if valid range
            if left_start <= left_end:
                mid = (left_start + left_end) // 2
                node.left = TreeNode(nums[mid])
                stack.append((node.left, left_start, mid - 1, mid + 1, left_end))
            
            # Process right subtree if valid range
            if right_start <= right_end:
                mid = (right_start + right_end) // 2
                node.right = TreeNode(nums[mid])
                stack.append((node.right, right_start, mid - 1, mid + 1, right_end))
        
        return root
##########################################################################################
s = Solution()
print_inorder(s.sortedArrayToBST([-10,-3,0,5,9]))
# >>> <TreeNode> [0,-3,9,-10,None,5] 
# >>> <TreeNode> [0,-10,5,None,-3,None,9]
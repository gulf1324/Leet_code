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
# Wrong
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        stack = [(root, root.val)]  # Stack holds (node, sum_so_far)
        good_count, sum_so_far = 0, 0
        
        while stack:
            node, node_val = stack.pop()
            sum_so_far += node_val  # Update sum_so_far
            
            if targetSum == sum_so_far:
                good_count += 1
                sum_so_far -= node_val
            elif targetSum < sum_so_far:
                sum_so_far -= node_val

            if node.right:
                stack.append((node.right, node.right.val))  # Push right first to simulate recursion order
            if node.left:
                stack.append((node.left, node.left.val))  # Push left
            elif not node.left and not node.right:
                sum_so_far = 0

        return good_count
#################################################################################################################
# iterative 
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0

        stack = [(root, root.val, {0: 1})]  # (node, current sum, prefix_sums dict)
        count = 0

        while stack:
            node, curr_sum, prefix_sums = stack.pop()

            # count == 0 or 1
            # ex) [(5, 15, {0:1, 10:1})]
            # prefix_sums[7] = 0 (No valid paths found)
            count += prefix_sums.get(curr_sum - targetSum, 0)
            
            new_prefix_sums = prefix_sums.copy()
            
            # 
            ##################################################################
            new_prefix_sums[curr_sum] = new_prefix_sums.get(curr_sum, 0) + 1 #
            # ex) [(5, 15, {0:1, 10:1})]                                     #
            ##################################################################

            if node.left:
                stack.append((node.left, curr_sum + node.left.val, new_prefix_sums))
            if node.right:
                stack.append((node.right, curr_sum + node.right.val, new_prefix_sums))

        return count
#################################################################################################################
# recursive
from collections import defaultdict
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # Base case: A path sum that directly equals targetSum
        
        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            count = prefix_sums[curr_sum - targetSum]  # Count paths that sum to targetSum
            ############################
            prefix_sums[curr_sum] += 1 #
            ############################
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            prefix_sums[curr_sum] -= 1
            
            return count
        
        return dfs(root, 0)
#################################################################################################################

# test case #1
root = build_tree([10,5,-3,3,2,None,11,3,-2,None,1])
s = Solution()
print("Number of paths:", s.pathSum(root, targetSum = 8))
# >>> 3

# test case #2
root = build_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])
s = Solution()
print("Number of paths:", s.pathSum(root, targetSum = 22))
# >>> 3
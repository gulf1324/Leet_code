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
from collections import defaultdict
##########################################################################################
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
##################################################################################    
root = build_tree([10,5,-3,3,2,None,11,3,-2,None,1])
s = Solution()
print(s.pathSum(root = root, targetSum = 8))
# >>> 3
# >>> [5,3], [5,2,1], [-3,11]
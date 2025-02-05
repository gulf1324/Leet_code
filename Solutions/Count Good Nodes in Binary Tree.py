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
##########################################################################################################
# recursive
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far) -> int: 
            if not node:
                return 0
            
            good = 0
            if node.val >= max_so_far:
                good = 1
                max_so_far = node.val

            #####################################
            good += dfs(node.left, max_so_far)  #
            good += dfs(node.right, max_so_far) #
            #####################################
            
            return good

        return dfs(root, root.val)
##########################################################################################################    
# iterative
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, root.val)]  # Stack holds (node, max_so_far)
        good_count = 0

        while stack:
            node, max_so_far = stack.pop()

            if node.val >= max_so_far:
                good_count += 1
                max_so_far = node.val  # Update max_so_far

            if node.right:
                stack.append((node.right, max_so_far))  # Push right first to simulate recursion order
            if node.left:
                stack.append((node.left, max_so_far))  # Push left

        return good_count
##########################################################################################################
# root = build_tree([3,3,None,4,2])
# >>> 3
root = build_tree([3,1,4,3,None,1,5])
# >>> 4
s = Solution()
print("Good Nodes:", s.goodNodes(root))
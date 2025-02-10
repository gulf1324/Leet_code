###################################
# build_tree #1
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
###################################
# build tree #2
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def build_tree(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    
    i = 1
    while i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root
###################################

from typing import Optional
####################################################################################################
# 1st attempt
# dfs_target_node : returns a list of path for the target_node
# lowestCommonAncestor : returns the LCA node for input 2 nodes
class Solution:
    def dfs_target_node(self, node:TreeNode, target_node:TreeNode) -> list:
        path = []
        def dfs(node):
            if not node:
                return False
            # test
            # path.append(node.val)
            path.append(node)
            
            if node.val == target_node.val:
                return True  
            
            #######################################
            if dfs(node.left) or dfs(node.right): #
                return True                       #
            #######################################

            path.pop()  # Remove the last node if target not found in this path
            return False
        
        dfs(node)
        return path if path else None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # ex) p = [3,1,0], q = [3,1,8]
        # >>> Treenode(1)
        p_route:list = self.dfs_target_node(root, p)
        q_route:list = self.dfs_target_node(root, q)
        for i in range(min(len(p_route), len(q_route)) - 1, -1, -1):
            if p_route[i] == q_route[i]:
                # test
                return p_route[i].val
                return p_route[i]
####################################################################################################
# Comparing the TreeNode itself
class Solution2:
    # for test
    def findNode(self, root: TreeNode, value: int) -> TreeNode:
        if not root:
            return None
        if root.val == value:
            return root
        left = self.findNode(root.left, value)
        if left:
            return left
        return self.findNode(root.right, value)
    
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root 
        left = self.lowestCommonAncestor(root.left, p, q)  
        right = self.lowestCommonAncestor(root.right, p, q)  

        if left and right:
            # test 
            # return root.val
            return root 
        
        return left if left else right 
####################################################################################################
root = build_tree([3,5,1,6,2,0,8,None,None,7,4])


s = Solution()
print("Target path:", s.dfs_target_node(root, TreeNode(0)))
print("LCA:", s.lowestCommonAncestor(root, TreeNode(0), TreeNode(8)))


s = Solution2()
node_0 = s.findNode(root, 0)
node_8 = s.findNode(root, 8)
print("LCA:", s.lowestCommonAncestor(root, node_0, node_8))

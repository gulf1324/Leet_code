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
# Wrong
from typing import Optional
class Solution:
    def bfs(self, root) -> list[TreeNode]:
        if not root:
            return []
        queue = [root]
        i = 0
        while i < len(queue):
            node = queue[i]
            if node:  
                queue.append(node.left if node.left else None)
                queue.append(node.right if node.right else None)
            i += 1
        while queue and queue[-1] is None:
            queue.pop()
        return queue
    
    def get_right_side_view(self, bfs_list)-> list[int]:
        if not bfs_list:
            return []
        
        res = []
        level_start = 0
        level_size = 1
        
        while level_start < len(bfs_list):
            # Find the rightmost non-None value in current level
            level_end = min(level_start + level_size, len(bfs_list))
            
            # Search from right to left in current level
            for i in range(level_end - 1, level_start - 1, -1):
                if bfs_list[i] is not None:
                    res.append(bfs_list[i].val)
                    break
            
            level_start += level_size
            level_size *= 2
        return res
    
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        
        queue = self.bfs(root)
        # test
        # print([i.val if i else None for i in queue])
        res = self.get_right_side_view(queue)
        
        return res
##########################################################################################################
# Not using None 
from collections import deque
class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()
                
                # If it's the last node in this level, add its value to the result
                # if i == level_size - 1:
                #     result.append(node.val)
                
                # Add children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # last node in this level, add its value to the result
            result.append(node.val)
        
        return result
##########################################################################################################
# root = build_tree([1,2,3,4,None,None,None,5])
root = build_tree([3,5,1,6,2,0,8,None,None,7,4])
# >>> [1,3,4,5]
s = Solution()
print("rightSideView:", s.rightSideView(root))


# def bfs_with_none(root) -> list:
#     if not root:
#         return []
        
#     result = []
#     queue = deque([root])
    
#     while queue:
#         node = queue.popleft()
        
#         if node:
#             result.append(node.val)
#             # Add both children (or None) to maintain structure
#             queue.append(node.left if node.left else None)
#             queue.append(node.right if node.right else None)
#         else:
#             result.append(None)
            
#     # Trim trailing Nones
#     while result and result[-1] is None:
#         result.pop()    
#     return result
# print(bfs_with_none(root))
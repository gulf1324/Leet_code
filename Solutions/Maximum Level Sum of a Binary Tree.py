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
from collections import defaultdict, deque
##########################################################################################################
# Accumulated sum of nodes until that level 
class Solution1:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sum_level_dict = defaultdict(int)
        queue = deque([root])
        level_sum = 0
        level = 1
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.popleft()
                level_sum += node.val
            
                if i == level_size - 1:
                    sum_level_dict[level] = level_sum
                    level += 1
                
                # print(sum_level_dict)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return max(sum_level_dict, key = sum_level_dict.get)
##########################################################################################################
# Sum of nodes on that level
# -> Create dict, find max val 
class Solution2:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sum_level_dict = defaultdict(int)
        queue = deque([root])
        level = 1

        while queue:
            level_size = len(queue)
            level_sum = 0
            for i in range(level_size):
                node = queue.popleft()
                level_sum += node.val
            
                if i == level_size - 1:
                    sum_level_dict[level] = level_sum
                    level += 1
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                # print(sum_level_dict)
        
        return max(sum_level_dict, key = sum_level_dict.get)
##########################################################################################################
# Update level/max_sum and return
# More efficient
class Solution3:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        level = 1
        min_level = level
        max_sum = float("-inf")

        while queue:
            level_size = len(queue)
            level_sum = 0
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            if max_sum < level_sum:
                max_sum = level_sum
                min_level = level
            
            level += 1
            # print(min_level)
        
        return min_level
##########################################################################################################
# root = build_tree([1,7,0,7,-8,None,None])
# Solution1 
# >>> defaultdict(<class 'int'>, {1: 1, 2: 8, 3: 7})
# >>> 2 
# Solution2
# >>> defaultdict(<class 'int'>, {1: 1, 2: 7, 3: -1})
# >>> 2

root = build_tree([989,None ,10250,98693,-89388,None,None,None,-32127])
# Solution1 
# >>> defaultdict(<class 'int'>, {1: 989, 2: 11239, 3: 20544, 4: -11583})
# >>> 3
# Solution2
# >>> defaultdict(<class 'int'>, {1: 989, 2: 10250, 3: 9305, 4: -32127})
# >>> 2

# root = build_tree([1,1,0,7,-8,-7,9])
# Solution1 
# >>> defaultdict(<class 'int'>, {1: 1, 2: 2, 3: 3})
# >>> 3
# Solution2
# >>> defaultdict(<class 'int'>, {1: 1, 2: 1, 3: 1})
# >>> 1

s = Solution3()
print("Sum-max-level:", s.maxLevelSum(root))
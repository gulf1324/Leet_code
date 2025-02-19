class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        visited = set()
        changed = 0
        to_zero = set({0})
        for connection in connections:
            if tuple(connection) in visited:
                continue
            
            visited.add(tuple(connection))
            i, j = connection

            if i in to_zero :
                changed +=1
                to_zero.add(j)
            if j in to_zero :
                to_zero.add(i)
        return changed
#############################################################################
# Use dictionary when 2nd check of a list is needed
from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        graph = defaultdict(list)

        for a, b in connections:
            graph[a].append((b, 1))  # 1 ==> a to b 
            graph[b].append((a, 0))  # 0 ==> b from a 
            # ex) 
            # defaultdict(<class 'list'>, 
            #            {0: [(1, 1), (4, 0)],
            #             1: [(0, 0), (3, 1)],
            #             3: [(1, 0), (2, 0)],
            #             2: [(3, 1)],
            #             4: [(0, 1), (5, 1)],
            #             5: [(4, 0)]})

        # dfs
        def dfs(city, parent):
            count = 0
            for neighbor, needs_reversal in graph[city]:
                if neighbor == parent:
                    continue  # Skip the parent node
                count += needs_reversal  
                count += dfs(neighbor, city)  # Recursively check other nodes
            return count
        return dfs(0, -1)        
#############################################################################        
s = Solution()
print(s.minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]))
# >>> 3

print(s.minReorder(n = 6, connections = [[4,5],[0,1],[1,3],[2,3],[4,0]]))
# >>> 3
        
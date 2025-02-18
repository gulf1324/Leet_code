##################################################################################################################
# Wrong 1
import numpy as np
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        size = len(isConnected[0])
        connection_count = 0
        connection_count = sum(isConnected[i][j] != np.eye(size)[i][j] for i in range(size) for j in range(size))
        return (1 if int(size - connection_count//2) <= 0 else int(size - connection_count//2))
##################################################################################################################
# Wrong 2
class Solution2:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        rows_visited = set()
        stack = [0]
        while stack:
            ###################
            row = stack.pop() #
            ###################
            if row in rows_visited:
                continue
            rows_visited.add(row)
            for connection, TF in enumerate(isConnected[row]):
                if connection not in rows_visited and TF:
                    stack.append(connection)
        return len(isConnected) - len(rows_visited) + 1 
##################################################################################################################
# Correct
class Solution3:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        rows_visited = set()
        provinces = 0
        
        # Cover all cities
        for city in range(len(isConnected)):
            
            if city in rows_visited:
                continue
            
            # else:
            provinces +=1
            stack = [city]
            while stack:
                ###################
                row = stack.pop() #
                ###################
                if row in rows_visited:
                    continue
                rows_visited.add(row)
                for connection, TF in enumerate(isConnected[row]):
                    if connection not in rows_visited and TF:
                        stack.append(connection)
        return provinces
##################################################################################################################
s = Solution3()
print(s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
print(s.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))
print(s.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))
# Wrong2
print(s.findCircleNum([[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
    [0,1,0,1,0,0,0,0,0,0,0,0,0,1,0],
    [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
    [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]))
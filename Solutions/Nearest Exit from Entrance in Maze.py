from collections import defaultdict, deque
############################################################################################## 
# From scratch (Correct, inefficient)
class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        maze_d = defaultdict(dict)

        for row_i, row in enumerate(maze):
            for column_i, column in enumerate(row):
                maze_d[row_i][column_i] = column

        # defaultdict(<class 'dict'>, 
        # {0: {0: '+', 1: '+', 2: '.', 3: '+'}, 
        #  1: {0: '.', 1: '.', 2: '.', 3: '+'},
        #  2: {0: '+', 1: '+', 2: '+', 3: '.'}})
        
        def bfs(start):
            steps = 0
            stack = deque([[start, steps]]) # list[list[int], int]
            visited = set()
            
            while stack:
                location, steps = stack.popleft()
                r, c = location 
                if tuple(location) in visited:
                    continue
                
                visited.add(tuple(location))
                
                if (0 in location or len(maze)-1 == r or len(maze[0])-1 == c) and location != start:
                    return steps
                steps +=1
                
                # up
                if maze_d.get(r-1, {}).get(c) == '.' and (r-1, c) not in visited:
                    stack.append([[r-1, c], steps])
                # right
                if maze_d.get(r, {}).get(c+1) == '.' and (r, c+1) not in visited:
                    stack.append([[r, c+1], steps])
                # down
                if maze_d.get(r+1, {}).get(c) == '.' and (r+1, c) not in visited:
                    stack.append([[r+1, c], steps])
                # left
                if maze_d.get(r, {}).get(c-1) == '.' and (r, c-1) not in visited:
                    stack.append([[r, c-1], steps])
            return -1
        
        return bfs(entrance)
############################################################################################## 
# Efficient
# * defaultdict ==> simple indexing
# * visited ==> change to '+' once visited
# * appending ([[node, steps]]) to a stack in every loop ==> while-for loop
# * redundant direction check ==> for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]
# *

# Shortest path in a maze -> bfs
class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        m, n = len(maze), len(maze[0])
        queue = deque([entrance])  
        
        maze[entrance[0]][entrance[1]] = '+'
        stepCounter = 0

        """ 
        while-for loop in BFS:
        while  → Keeps running until all nodes are processed.
        for  → Iterates through the 'current level' of nodes before moving to the next level
        """
        ## BFS & level-wise check => "while-for loop" ##
        while queue:                                   #
            stepCounter += 1                           #
            for _ in range(len(queue)):                #
        ################################################
                row, col = queue.popleft()
                # up, down, left, right
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    x, y = row + dx, col + dy
                    if 0 <= x < m and 0 <= y < n and maze[x][y] == ".":
                        if x == 0 or y == 0 or x == m-1 or y == n-1:
                            return stepCounter  
                        queue.append((x, y))
                        maze[x][y] = "+"    # inaccessible once visited                
        return -1       
############################################################################################## 
s = Solution()
print(s.nearestExit(maze = [["+","+",".","+"],
                            [".",".",".","+"],
                            ["+","+","+","."]], 
                    entrance = [1,2]))
# # >>> 1

print(s.nearestExit(maze = [["+","+","+"],
                            [".",".","."],
                            ["+","+","+"]],
                    entrance = [1,0]))
# # >>> 2

print(s.nearestExit(maze = [[".","+"]], 
                    entrance = [0,0]))
# >>> -1

print(s.nearestExit(maze = [["+",".","+","+","+","+","+"],
                            ["+",".","+",".",".",".","+"],
                            ["+",".","+",".","+",".","+"],
                            ["+",".",".",".","+",".","+"],
                            ["+","+","+","+","+",".","+"]], 
                    entrance = [0,1]))
# >>> 12 

print(s.nearestExit(maze = [["+",".","+","+","+","+","+"],
                            ["+",".","+",".",".",".","+"],
                            ["+",".","+",".","+",".","+"],
                            ["+",".",".",".",".",".","+"],
                            ["+","+","+","+",".","+","."]],
                    entrance = [0,1]))
# >>> 7 but 10
# Error when there's fork in path, ```steps``` added to stack
# >>> 7

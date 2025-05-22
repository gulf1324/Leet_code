from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        minute_counter = 0
        queue = deque()
        
        # find rotten orange
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                if value == 2:
                    queue.append([i, j])
        
        # bfs by minute
        while queue:
            any_rot = False
            for _ in range(len(queue)):
                x_, y_ = queue.popleft()
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    x, y = x_ + dx, y_ + dy
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        queue.append((x,y))
                        any_rot = True
            # if any oranges rot
            if any_rot :
                minute_counter +=1
        
        return minute_counter if not any(1 in row for row in grid) else -1
################################################################################
s= Solution()
print(s.orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]]))
# >>> 4
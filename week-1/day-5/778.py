# Swim In Rising Water.

import heapq

class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        pq = [(grid[0][0], 0, 0)]
        visited = set((0, 0))
        
        while pq:
            elevation, x, y = heapq.heappop(pq)
            if x == n - 1 and y == n - 1:
                return elevation
          
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    heapq.heappush(pq, (max(elevation, grid[nx][ny]), nx, ny))
                    
        return -1

grid = [[0,2],[1,3]]
solution = Solution()
print(solution.swimInWater(grid))  

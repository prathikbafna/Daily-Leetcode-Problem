"""

417. Pacific Atlantic Water Flow
Solved
Medium
Topics
premium lock icon
Companies
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

"""

class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        R=len(grid)
        C=len(grid[0])
        res=[]
        pacific=[]
        atlantic=[]

        #right and left side
        for r in range(R):
            pacific.append((r,0,grid[r][0]))
            atlantic.append((r,C-1,grid[r][C-1]))
        #north and south side
        for c in range(C):
            pacific.append((0,c,grid[0][c]))
            atlantic.append((R-1,c,grid[R-1][c]))

        #pacific bfs
        pacific_reach=set()
        while pacific:
            r, c, h = pacific.pop()
            if (r, c) in pacific_reach:
                continue
            pacific_reach.add((r, c))
            nei = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
            for nr, nc in nei:
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] >= h:
                    pacific.append((nr, nc, grid[nr][nc]))
        

        #atlantic bfs
        atlantic_reach=set()
        while atlantic:
            r, c, h = atlantic.pop()
            if (r, c) in atlantic_reach:
                continue
            atlantic_reach.add((r, c))
            nei = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
            for nr, nc in nei:
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] >= h:
                    atlantic.append((nr, nc, grid[nr][nc]))
        for r,c in pacific_reach:
            if (r,c) in atlantic_reach:
                res.append((r,c))
        return res
        
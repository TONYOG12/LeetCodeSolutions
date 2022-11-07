class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0]) 
        visit = set()
        count = 0
        
        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            
            while q:
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                row, col = q.popleft()
                
                for dr, dc in directions:
                    r , c = row + dr, col + dc
                    if(r in range(rows)
                       and c in range(cols)
                       and grid[r][c] == "1"
                       and (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))
                        
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in visit:
                    bfs(row, col)
                    count += 1
                    
        return count

                

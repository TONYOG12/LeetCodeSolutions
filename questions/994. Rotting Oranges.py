class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        visited = set()
        q = collections.deque()


        def bfs(row, col):

            visited.add((row, col))
            q.append((row, col))

            

        rows, cols = len(grid), len(grid[0])
        minutes = 0
        fresh = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))

                if grid[row][col] == 1:
                    fresh += 1
                    
        while fresh > 0 and q:

            for i in range(len(q)):
                r, c = q.popleft()

                directions = [[0,1], [0,-1], [1,0], [-1, 0]]

                for dr, dc in directions:
                    nr, nc = r+ dr, c + dc

                    if(nr in range(rows) and
                        nc in range(cols) and
                        grid[nr][nc] == 1):

                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
                    

            minutes += 1

        return minutes if fresh == 0 else -1

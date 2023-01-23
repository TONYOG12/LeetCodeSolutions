class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        rows, cols = len(mat), len(mat[0])
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):

                if mat[r][c] == 0:
                    q.append((r, c))

                else:
                    mat[r][c] = "#"


        

        while q:

            r, c = q.popleft()

            directions = [[0,1], [0, -1], [1,0], [-1,0]]


            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if(nr in range(rows) and
                   nc in range(cols) and
                   mat[nr][nc] == "#"):

                   mat[nr][nc] = mat[r][c] + 1
                   q.append((nr, nc))

        
        return mat



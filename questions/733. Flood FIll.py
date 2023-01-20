class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        visited = set()
        q = collections.deque()

        def bfs(sr, sc):

            visited.add((sr, sc))
            q.append((sr, sc))

            sourceImage = image[sr][sc]


            while q:

                r, c = q.popleft()
                image[r][c] = color

                directions = [[0,1], [0,-1], [1,0], [-1,0]]

                for dr, dc in directions:

                    nr, nc = r + dr, c + dc


                    if(nr in range(rows) and 
                    nc in range(cols) and 
                    (nr,nc) not in visited and 
                    image[nr][nc] == sourceImage):
                        q.append((nr, nc))
                        visited.add((nr, nc))


        rows, cols = len(image), len(image[0])

        bfs(sr, sc)

        return image

        

       





            








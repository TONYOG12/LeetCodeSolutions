class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = [[0 for y in range(n)] for x in range(m)]
  
        for i in range(m):
            for j in range(n):
            
                memo[i][j] = -1
              
        #recursive function 
        return self.numOfPathsToSquare(m-1, n-1, memo)



    def numOfPathsToSquare(self, i , j, memo):
        
        if i < 0 or j < 0:
            return 0
        
        #check to see if we have already visited that path, saves uneccesary function calls
        elif memo[i][j] != -1:
            return memo[i][j]
        
        #base condition, number of paths to edges will always be 1
        elif i == 0:
            memo[i][j] = 1

        else:
                          #we check the up and left neighbours and find out number of paths to them recursivelly
            memo[i][j] = self.numOfPathsToSquare(i - 1, j , memo) + self.numOfPathsToSquare(i, j-1, memo)

        return memo[i][j]


    
        

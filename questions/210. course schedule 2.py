class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = dict()
        for i in range(numCourses):
            graph[i] = list()
            
        for course in prerequisites:
            a , b = course
            graph[a].append(b)
                
        
        res = list()
        visited = set()
        cycle = set()
        
        def dfs(c):
            
            if c in visited:
                return True
            
            if c in cycle:
                return False
            
            cycle.add(c)
            for neigh in graph[c]:
                if not dfs(neigh):
                    return False
            
            cycle.remove(c)
            visited.add(c)
            res.append(c)
            return True
            
            
        for crs in range(numCourses):
            if not dfs(crs):
                return []
            
        return res
                    
                
            
                
            
            

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #function to check if we can complete course
        def courseStatus(c):
            
            #if course has been visited already implies a cycle hence we should return False
            if c in visited:
                return False
            
            #if course has no prerequisites we can do it
            if graph[c] == []:
                return True
            
            visited.add(c)
            
            for neigh in graph[c]:
                if not courseStatus(neigh):
                    return False
                
            visited.remove(c)
            graph[c] = list()
            return True
        
        
        
        #creating our graph
        graph = dict()
        visited = set()
        
        for i in range(numCourses):
            graph[i] = list()
            
        for course in prerequisites:
            a,b = course
            graph[a].append(b)
            
        for c in range(numCourses):
            if not courseStatus(c):
                return False
        return True
        
        
        
        
               
        
            
        
        
        

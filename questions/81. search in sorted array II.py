class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        #return true if index of target value exists in array
        try:
            #python sees 0 as false so need to check for that index
            if nums.index(target) == 0:
                return True
            return nums.index(target)
        except:
            return False
        
        
        #Time Complexity = O(n)
        #Space Complexity = 0(1)
        
        #Utilize binary search for better time complexity
        

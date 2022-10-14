class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        try:
            if nums.index(target) == 0:
                return True
            
            return nums.index(target)
        except:
            return False
        

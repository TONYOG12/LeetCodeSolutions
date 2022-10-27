class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #sort the list
        nums.sort()
        ls = list()

        
        
        for i, num in enumerate(nums):
            
            #if two values are consecutively the same we want to skip the three sum operation
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            #initialize two counters that check for the two other sums
            l = i+ 1
            r = len(nums) -1
            
            while l < r:
                
                threeSum = num + nums[l] + nums[r]
                
    #three sum is larger than 0 so we need to decrease our right pointer to get a smaller value
            #works cos our list is sorted
                if threeSum > 0:
                    r -= 1
                    
                    
    #three sum is smaller than 0 so we need to increase our left pointer to get a larger value
                elif threeSum < 0:
                    l +=1

                else:
                    ls.append([num, nums[l], nums[r]])
                    l += 1

                    while nums[l] == nums[l-1] and l < r:
                        l+=1 
                
                
        return ls
            

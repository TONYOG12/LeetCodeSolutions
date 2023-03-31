class Solution(object):
    def searchInsert(self, nums, target):


        l, r = 0, len(nums) - 1
        res = 0


        while l <= r:


            m = (l + r)//2

            if nums[m] < target:
                l = m + 1
                res = m + 1


            elif nums[m] > target:
                r = m - 1
                res = m - 1

            else:
                return m

        return l


        '''        


        if res < 0:
            res = 0
        
        elif res > len(nums) - 1:
            res = len(nums) - 1
            
        if nums[res] > target: 
            return res

        elif nums[res] < target:
            return res + 1

        '''


        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

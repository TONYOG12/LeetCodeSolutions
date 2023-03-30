class Solution(object):
    def removeElement(self, nums, val):

        l, res = 0, 0

        for r in range(len(nums)):

            l = r


            while l < len(nums) - 1 and nums[l] == val:
                l += 1
                

            #swap both values
            nums[r], nums[l] = nums[l], nums[r] 


        for n in nums:

            if n == val:
                return res

            res += 1


        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

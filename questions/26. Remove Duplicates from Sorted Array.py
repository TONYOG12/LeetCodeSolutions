class Solution(object):
    def removeDuplicates(self, nums):

        l, res = 0, 0
        hashSet = set()

        for r in range(len(nums)):


            while l < len(nums) - 1 and nums[l] in hashSet:
                l += 1
                

            #swap both values
            nums[r], nums[l] = nums[l], nums[r] 

            hashSet.add(nums[r])

        
        hashSet = set()
        
        for n in nums:

            if n in hashSet:
                break

            hashSet.add(n)
            res += 1


        return res




        """
        :type nums: List[int]
        :rtype: int
        """

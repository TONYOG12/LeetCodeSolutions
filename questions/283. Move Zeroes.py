class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        l = 0

        for r in range(len(nums)):

            while l < len(nums) and nums[l] != 0:
                l += 1

            if r > l and nums[r] != 0:
                nums[r], nums[l] = nums[l], nums[r] #swap

            

        """
        Do not return anything, modify nums in-place instead.
        """

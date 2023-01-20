class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        res = float("-inf")
        arraySum = 0

        for r in range(len(nums)):

          
            arraySum += nums[r]

            res = max(res, arraySum)

            #greedy algorithm, we reset arraySum to 0 to avoid negative sums
            if arraySum < 0:
                arraySum = 0
                
        return res

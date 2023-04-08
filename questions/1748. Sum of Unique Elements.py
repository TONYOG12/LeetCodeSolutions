class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:

        count = Counter(nums)
        res = 0


        for num in nums:

            if count[num] == 1:
                res += num

        return res




                

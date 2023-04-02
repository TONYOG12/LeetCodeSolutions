class Solution(object):
    def singleNumber(self, nums):

        count = Counter(nums)

        for k in count:

            if count[k] == 1:
                return k
              
              
     def singleNumber2(self, nums):

        nums.sort()

        if len(nums) == 1:
            return nums[0]



        for i in range(len(nums) - 1):

            if i == 0 and nums[i] != nums[i + 1]:
                return nums[i]
               
            elif i == len(nums) - 1 and nums[i] != nums[i - 1]:
                return nums[i]
 
            elif nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                return nums[i]

        return nums[i +1]

            
        """
        :type nums: List[int]
        :rtype: int
        """

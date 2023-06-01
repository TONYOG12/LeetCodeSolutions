class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def quicksort(nums):

            if len(nums) < 2:
                return nums

            pivot = random.choice(nums)


            left = []
            equal = []
            right = []


            for num in nums:

                if num < pivot:
                    left.append(num)

                elif num > pivot:
                    right.append(num)

                else:
                    equal.append(num)

            return quicksort(left) + equal + quicksort(right)


        return quicksort(nums)





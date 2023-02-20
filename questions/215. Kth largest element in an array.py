class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums = [-i for i in nums]

        heapq.heapify(nums)

        while k > 1:
            heapq.heappop(nums)
            k -= 1

        return -nums[0]

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        countMap = Counter(arr)

        nums = list(countMap.values())
        
        heapq.heapify(nums)

        while k > 0 and k >= nums[0]:

            num = heapq.heappop(nums)

            k -= num

        
        return len(nums)






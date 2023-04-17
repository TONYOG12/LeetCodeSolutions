class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        res = 0
        

        hashMap = defaultdict(list)

        for i, num in enumerate(nums):
            hashMap[num].append(i)

        for arr in hashMap.values():

            #number of combinations of numbers taking 2 at a time formula
            n = len(arr)

            res += (n * (n - 1))//2

        return res

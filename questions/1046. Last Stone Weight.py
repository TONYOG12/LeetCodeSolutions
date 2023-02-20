class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-i for i in stones]

        heapq.heapify(stones)

        while len(stones) > 1:

            first, second = heapq.heappop(stones), heapq.heappop(stones)

            if first == second:
                continue

            heapq.heappush(stones, first - second)

        if stones:
            return abs(stones[0])


        return 0



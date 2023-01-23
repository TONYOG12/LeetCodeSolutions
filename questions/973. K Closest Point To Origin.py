class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        hashMap = defaultdict(list)
        freq = []
        res = []

        distance = 0

        for i in range(len(points)):

            distance = math.sqrt(pow(points[i][0], 2) + pow(points[i][-1], 2))
            freq.append(distance)

            hashMap[distance].append(points[i])

        
        freq.sort()


        for distance in freq:

            for point in hashMap[distance]:
                res.append(point)

                if len(res) == k:
                    return res





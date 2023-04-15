class Solution:
    def firstUniqChar(self, s: str) -> int:

        hashMap = defaultdict(list)

        res = []

        for r in range(len(s)):

            hashMap[s[r]].append(r)

        
        for arr in hashMap.values():

            if len(arr) == 1:
                res.extend(arr)



        return min(res) if res else -1


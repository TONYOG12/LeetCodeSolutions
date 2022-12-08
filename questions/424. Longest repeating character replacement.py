class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l, res = 0, 0

        hashMap = {}

        for r in range(len(s)):
            hashMap[s[r]] = 1 + hashMap.get(s[r], 0)

            maxf = max(hashMap.values())

            while (r - l + 1) - maxf > k:
                hashMap[s[l]] -= 1
                l += 1

            res = max(res, (r - l + 1))

        return res


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:


        if len(needle) > len(haystack):
            return -1

        l = 0

        start = len(needle) - 1


        for r in range(start, len(haystack)):

            if needle == haystack[l:r+1]:
                return l

            l += 1

        return -1

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        if n == 0:
            return 0


        l, r = 1, n 


        while l <= r:

            m = (l + r)//2


            if isBadVersion(m) and not isBadVersion(m-1):
                return m


            elif not isBadVersion(m):
                l = m + 1

            else:
                r = m - 1

            


class Solution:
    def mySqrt(self, x: int) -> int:

        l, r = 0, x
        res = 0

        while l <= r:

            m = (l + r)//2

            if m**2 == x:
                return m

            elif m**2 < x:
                res = m
                l = m + 1

            else:
                r = m - 1

        return res

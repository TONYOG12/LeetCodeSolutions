class Solution:
    def reverse(self, x: int) -> int:

        res = 0

        integer = x

        while x:

            val = abs(x) % 10
            res = (res * 10) + val
            x = (abs(x) - val)// 10


        if res > 2**31 - 1 or res < -2**31:
            return 0

        if integer < 0:
            return -res

        

        return res

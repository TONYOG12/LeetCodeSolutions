class Solution:
    def isHappy(self, n: int) -> bool:

        visit = set()

        while n not in visit:

            visit.add(n)

            n = self.sumOfNumber(n)

            if n == 1:
                return True

        return False


    def sumOfNumber(self, n):

            res = 0

            while n:
                value = n % 10
                res += value **2
                n //= 10

            return res


    

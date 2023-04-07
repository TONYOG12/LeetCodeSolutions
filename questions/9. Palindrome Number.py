class Solution:
    def isPalindrome(self, x: int) -> bool:


        if x < 0:
            return False

        stack = []

        length = 0


        while x:

            val = x % 10

            stack.append(val)

            x = (x - val) //10



        l, r = 0, len(stack) - 1


        while l < r:


            if stack[l] != stack[r]:
                return False

            l += 1
            r -= 1


        return True

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        num1 = int(a)
        num2 = int(b)

        carry = 0
        res = ""

        if a == "0" and b =="0":
            return "0"

        while num1 or num2 or carry:

            numA = num1 % 2
            numB = num2 % 2

            val = numA + numB + carry

            res += str((val % 2))

            carry =  val//2


            num1 = (num1)//10
            num2 = (num2)//10
    

        return res[::-1]

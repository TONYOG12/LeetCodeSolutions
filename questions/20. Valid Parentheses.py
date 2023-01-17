class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {")":"(", "}":"{", "]":"["}


        stack = list()


        for item in s:

            if item in brackets and stack:

                br = stack.pop()
                if br != brackets[item]:
                    return False
            
            else:
                stack.append(item)


        return not stack
        

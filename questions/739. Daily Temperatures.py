class Solution(object):
    def dailyTemperatures(self, temperatures):

        stack = []
        res = [0 for i in range(len(temperatures))]


        for i, value in enumerate(temperatures):

            while stack and stack[-1][0] < value:
                val, ind = stack.pop()
                res[ind] = i - ind
        
            stack.append((value, i))


        return res
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

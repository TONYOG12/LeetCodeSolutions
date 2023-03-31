class Solution(object):
    def plusOne(self, digits):


        my_list = "".join(map(str, digits))

        value = int(my_list)

        value = value + 1

        res = [int(ch) for ch in str(value)]

        return res
        """
        :type digits: List[int]
        :rtype: List[int]
        """

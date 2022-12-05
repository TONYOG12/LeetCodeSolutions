class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):

        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res


        # write your code here

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):

        res, i = [], 0


        while i < len(str):

            j = i

            while str[j] != "#":
                j += 1

            length =  int(str[i:j])

            word = str[j+1: length]

            res.append(word)

            i = j + 1 + length

        
        return res



       
        # write your code here

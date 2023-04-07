class Solution:
    def lengthOfLastWord(self, s: str) -> int:


        ls = s.split()


        return len(ls[-1])

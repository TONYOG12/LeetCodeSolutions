class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        hashMap = {}
   
        if len(t) != len(s):
            return False

        
        for i in range(len(s)):

            if s[i] in hashMap and hashMap[s[i]] != t[i]:
                return False

            if s[i] not in hashMap and t[i] in hashMap.values():
                return False

            hashMap[s[i]] = t[i]
            
        return True



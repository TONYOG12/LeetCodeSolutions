class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #if words are not of the same length they cant be anagrams
        if len(s) != len(t):
            return False
        
        
        
        hashMap = dict()
        count = dict()
     
        
        #use hashmap to keep track of number of times each letter in a word occurs
        for item in s:
            if item in hashMap:
                hashMap[item] += 1
                continue
                
            hashMap[item] = 1
            count[item] = 0
            
        #if letter not in hashMap return false    
        for item in t:
            if item not in hashMap:
                return False
         #count how many times a letter occurs in second word  
            else:
                count[item] += 1
                
    #if number of times letters appear in both words do not add up the words cant be an anagram
                
        for item in s:
            if count[item] != hashMap[item]:
                return False
                
        return True

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(ransomNote) > len(magazine):
            return False


        count1 = {}
        count2 = {}


        for c in ransomNote:
            count1[c] = count1.get(c, 0) + 1

        for s in magazine:
            count2[s] = count2.get(s,0) + 1


        for letter in ransomNote:

            if letter not in count2 or count1[letter] > count2[letter]:
                return False

        return True

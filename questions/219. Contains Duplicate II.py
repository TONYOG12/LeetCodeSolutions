
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hashMap = dict()
        
        for i, num in enumerate(nums):
            
            if num in hashMap and abs(hashMap[num] - i) <= k:
                return True
            
            hashMap[num] = i
            
        return False





class Solution2:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hashMap = defaultdict(list)


        for i, val in enumerate(nums):

            if val in hashMap:

                if abs(hashMap[val][-1] - i) <= k:
                    return True

                hashMap[val].pop()
             
            hashMap[val].append(i)


        return False




            
        

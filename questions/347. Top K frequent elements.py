class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        freq = [[] for i in range(len(nums) + 1)]
        
        count = {}
        
        for num in nums:
            
            count[num] = count.get(num, 0) + 1
            
            
        for n, c in count.items():
            freq[c].append(n)
            
        for i in range(len(freq) - 1, 0 , -1):
            
            for item in freq[i]:
                
                res.append(item)
                
                if len(res) == k:
                    return res
            
            

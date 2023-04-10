class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        hashMap = {}
        res = []


        for r in range(len(nums2)):

            l = r + 1

            while l in range(len(nums2)) and nums2[l] < nums2[r]:
                l += 1

            if l in range(len(nums2)) and nums2[l] > nums2[r]:
                hashMap[nums2[r]] = nums2[l]

            else:
                hashMap[nums2[r]] = -1


        
        for num in nums1:
            res.append(hashMap[num])

        return res



            

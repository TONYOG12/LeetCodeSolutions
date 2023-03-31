class Solution(object):
    def merge(self, nums1, m, nums2, n):

        if n == 0:
            return

        if m == 0 and len(nums1) == 0:
            nums1[0] = nums2[0]
            return


        for i in range(m, len(nums1)):

            nums1[i] = nums2[(i - n)%n]

        nums1.sort()



        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

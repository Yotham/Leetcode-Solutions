class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        merged = []
        i = 0
        k = 0
        while(i < m):
            merged.append(nums1[i])
            i+=1
        while(k < n):
            merged.append(nums2[k])
            k+=1
        merged = sorted(merged)
        for i in range(len(nums1)):
            nums1[i] = merged[i]
        
        return None
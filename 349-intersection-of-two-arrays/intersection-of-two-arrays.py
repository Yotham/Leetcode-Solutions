class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        storage = set(nums2+nums1)
        final = []
        for num in storage:
            if num in nums1 and num in nums2:
                final.append(num)
        return final
        
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        storage = set()
        for num in (nums1 + nums2):
            if num in nums1 and num in nums2:
                storage.add(num)
        return list(storage)
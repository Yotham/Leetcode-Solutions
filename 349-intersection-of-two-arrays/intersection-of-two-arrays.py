class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        storage = []
        for num in (nums1 + nums2):
            if num in nums1 and num in nums2:
                if num not in storage:
                    storage.append(num)
        return storage
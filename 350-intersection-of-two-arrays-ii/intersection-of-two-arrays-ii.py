class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        storage = {}
        for num in nums1 + nums2:
            if num in nums1 and num in nums2:
                if num not in storage:
                    storage[num] = 1
                else:
                    if storage[num] < nums1.count(num) and storage[num] < nums2.count(num):
                        storage[num] += 1
        store = []
        for key,val in storage.items():
            for i in range(val):
                store.append(key)
        return store
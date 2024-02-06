import operator
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        maxCount = 0
        for num in set(nums):
            count = nums.count(num)
            counts[num] = count
            maxCount = max(maxCount,count)
        out = []
        while True:
            if k == 0:
                break
            for key in counts.keys():
                if counts[key] == maxCount:
                    out.append(key)
                    k-=1
            maxCount-=1
            
        return out
                    
        
        
        
        



        
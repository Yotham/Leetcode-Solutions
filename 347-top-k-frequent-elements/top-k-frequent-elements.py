import operator
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        for num in set(nums):
            count = nums.count(num)
            counts[num] = count
        counts = sorted(counts.items(), key = lambda x :x[1],reverse = True)
        return [item[0] for item in counts[:k]]
                    
        
        
        
        



        
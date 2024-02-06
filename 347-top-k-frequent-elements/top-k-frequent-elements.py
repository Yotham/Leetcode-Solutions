import operator
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = defaultdict(int)
        for num in set(nums):
            counts[num] = nums.count(num)
        return [item[0] for item in sorted(counts.items(), key = lambda x :x[1],reverse = True)[:k]]
                    
        
        
        
        



        
import operator
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        return [item[0] for item in sorted(counts.items(), key = lambda x :x[1],reverse = True)[:k]]
                    
        
        
        
        



        
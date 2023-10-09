class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        stored = []
        Max = float('-inf')
        ret = None
        for item in nums:
            if item not in stored:
                count = nums.count(item)
                if count > Max:
                    print(item,count)
                    ret = item
                    Max = count
                stored.append(item)


                
        return ret
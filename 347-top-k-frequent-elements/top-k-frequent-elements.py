class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        out = {}
        for num in set(nums):
            out[num] = nums.count(num)
        print(out)
        sortedOut = sorted(out.items(), key=lambda x:x[1], reverse = True)
        final = []
        print(sortedOut)
        for i in range(k):
            final.append(sortedOut[i][0])
        return final


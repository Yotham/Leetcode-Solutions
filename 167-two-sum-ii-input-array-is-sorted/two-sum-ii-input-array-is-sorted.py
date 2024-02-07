class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for i in range(len(numbers)):
            calc = target-numbers[i]
            if calc in hashMap:
                return [hashMap[calc],i+1]
            hashMap[numbers[i]] = i+1
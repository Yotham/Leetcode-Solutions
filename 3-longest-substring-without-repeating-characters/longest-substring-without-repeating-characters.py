class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l == 0:
            return 0
        seen = {}
        start = 0
        maxL = 0
        for i in range(l):
            if s[i] in seen and start <= seen[s[i]]:
                start = seen[s[i]]+1
            else:
                maxL = max(maxL,i-start+1)
            seen[s[i]] = i
        return maxL
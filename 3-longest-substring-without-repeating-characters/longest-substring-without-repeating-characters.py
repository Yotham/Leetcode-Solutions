class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        l = len(s)
        seen = {}
        maxL = 0
        startVal = 0 
        for i in range(l):
            if s[i] in seen and startVal <= seen[s[i]]:
                startVal = seen[s[i]]+1
            else:
                maxL = max(maxL,i-startVal+1)
            seen[s[i]] = i
        return maxL

            
        
        
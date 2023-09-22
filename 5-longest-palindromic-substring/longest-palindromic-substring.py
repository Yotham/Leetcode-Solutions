class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(string, i, j):
            while(i >= 0 and j < len(string) and string[i] == string[j]):
                i-=1
                j+=1
            return string[i+1:j]
        ret = ""
        for i in range(len(s)):
            ret = max(ret,expand(s,i,i),expand(s,i,i+1),key=len)
        return ret

        
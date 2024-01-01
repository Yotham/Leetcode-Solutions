class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        final = ""
        index = 0
        for letter in t:
            if letter in s:
                temp = final
                temp += letter
                if temp[index] == s[index]:
                    final+=letter
                    index += 1
        if s == final:
            return True
        return False
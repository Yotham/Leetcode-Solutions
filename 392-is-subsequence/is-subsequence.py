class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        compare = ""
        index =0
        for character in t:
            if character in s and compare.count(character) < s.count(character):
                if s[index] == character:
                    compare+=character
                    if index < len(s)-1:
                        index+=1
        print(compare)
        if compare == s:
            return True

        return False
                

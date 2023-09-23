class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        top = 0
        for i in range(len(s)):
            characters = []
            characters.append(s[i])
            for j in range(i+1,len(s)):
                if s[j] not in characters:
                    characters.append(s[j])
                else:
                    break
            newS = "".join(characters)
            if len(newS) > top:
                top = len(newS)

        return top

            
        
        
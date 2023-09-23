class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        strings = []
        for i in range(len(s)):
            characters = []
            characters.append(s[i])
            for j in range(i+1,len(s)):
                if s[j] not in characters:
                    characters.append(s[j])
                else:
                    break
            if "".join(characters) not in strings:
                strings.append("".join(characters))
        if strings == []:
            return 0 
        return len(max(strings,key=len))

            
        
        
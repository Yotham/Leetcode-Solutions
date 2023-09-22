class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magCount = {}
        for c in magazine:
            if c not in magCount.keys():
                magCount[c] = 1
            else:
                magCount[c] +=1
        for c in ransomNote:
            if c in magCount and magCount[c] >= 1:
                magCount[c] -= 1
            else:
                return False
            
        return True
        
         
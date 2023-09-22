class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magCount = {}
        ranCount = {}
        for c in magazine:
            if c not in magCount.keys():
                magCount[c] = 1
            else:
                magCount[c] +=1
        for c in ransomNote:
            if c not in ranCount.keys():
                ranCount[c] = 1
            else:
                ranCount[c] += 1


        for item in magCount.keys():
            if item in ranCount.keys():
                if magCount[item] >= ranCount[item]:
                    ranCount[item] = "Done"
                else:
                    ranCount[item] = "Nope"
        print(ranCount)
        for item in ranCount:
            if ranCount[item] != "Done":
                return False
        return True
        
         
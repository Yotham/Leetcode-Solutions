class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list) #mapping character count to list of anagrams

        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(word)
        
        return res.values()


        
